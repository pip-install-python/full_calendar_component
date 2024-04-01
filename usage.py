import full_calendar_component as fcc
from dash import *
import dash_mantine_components as dmc
import json
from dash.exceptions import PreventUpdate
from datetime import datetime, date
import dash_quill

app = Dash(__name__, prevent_initial_callbacks=True)

quill_mods = [
    [{"header": "1"}, {"header": "2"}, {"font": []}],
    [{"size": []}],
    ["bold", "italic", "underline", "strike", "blockquote"],
    [{"list": "ordered"}, {"list": "bullet"}, {"indent": "-1"}, {"indent": "+1"}],
    ["link", "image"],
    # ['clean'],
]

# Get today's date
today = datetime.now()

# Format the date
formatted_date = today.strftime("%Y-%m-%d")


app.layout = html.Div(
    [
        fcc.FullCalendarComponent(
            id="calendar",  # Unique ID for the component
            initialView="dayGridMonth",  # dayGridMonth, timeGridWeek, timeGridDay, listWeek,
            # dayGridWeek, dayGridYear, multiMonthYear, resourceTimeline, resourceTimeGridDay, resourceTimeLineWeek
            headerToolbar={
                "left": "prev,next today",
                "center": "title",
                "right": "dayGridMonth,timeGridWeek,timeGridDay",
            },  # Calendar header
            initialDate=f"2024-04-01",  # Start date for calendar
            editable=True,  # Allow events to be edited
            selectable=True,  # Allow dates to be selected
            events=[
                {
                    "title": "Pip Install Python",  # Event title
                    "start": f"{formatted_date}T07:00:00",  # Event start date
                    "end": f"{formatted_date}T10:00:00",  # Event end date
                    "className": "bg-gradient-success",  # Event color
                    "extendedProps": {
                        "context": "Pip Install FullCalendar",  # On event click body context
                    },
                },
            ],
            nowIndicator=True,  # Show current time indicator
            navLinks=True,  # Allow navigation to other dates
        ),
        dmc.Modal(
            id="modal",
            size="xl",
            title="Event Details",
            zIndex=10000,
            children=[
                html.Div(id="modal_event_display_context"),
                dmc.Space(h=20),
                dmc.Group(
                    [
                        dmc.Button(
                            "Close",
                            color="red",
                            variant="outline",
                            id="modal-close-button",
                        ),
                    ],
                    position="right",
                ),
            ],
        ),
        dmc.Modal(
            id="add_modal",
            title="New Event",
            size="xl",
            children=[
                dmc.Grid(
                    children=[
                        dmc.Col(
                            html.Div(
                                dmc.DatePicker(
                                    id="add_modal_date",
                                    label="Start Date",
                                    value=datetime.now().date(),
                                    styles={"width": "100%"},
                                    disabled=True,
                                ),
                                style={"width": "100%"},
                            ),
                            span=6,
                        ),
                        dmc.Col(
                            html.Div(
                                dmc.TextInput(
                                    label="Event Name:",
                                    style={"width": "100%"},
                                    id="event_name_input",
                                    required=True,
                                ),
                                style={"width": "100%"},
                            ),
                            span=6,
                        ),
                    ],
                    gutter="xl",
                ),
                dmc.Select(
                    label="Select event color",
                    placeholder="Select one",
                    id="event_color_select",
                    value="ng",
                    data=[
                        {
                            "value": "bg-gradient-primary",
                            "label": "bg-gradient-primary",
                        },
                        {
                            "value": "bg-gradient-secondary",
                            "label": "bg-gradient-secondary",
                        },
                        {
                            "value": "bg-gradient-success",
                            "label": "bg-gradient-success",
                        },
                        {"value": "bg-gradient-info", "label": "bg-gradient-info"},
                        {
                            "value": "bg-gradient-warning",
                            "label": "bg-gradient-warning",
                        },
                        {"value": "bg-gradient-danger", "label": "bg-gradient-danger"},
                        {"value": "bg-gradient-light", "label": "bg-gradient-light"},
                        {"value": "bg-gradient-dark", "label": "bg-gradient-dark"},
                        {"value": "bg-gradient-white", "label": "bg-gradient-white"},
                    ],
                    style={"width": "100%", "marginBottom": 10},
                    required=True,
                ),
                dash_quill.Quill(
                    id="rich_text_input",
                    modules={
                        "toolbar": quill_mods,
                        "clipboard": {
                            "matchVisual": False,
                        },
                    },
                ),
                dmc.Accordion(
                    children=[
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Raw HTML"),
                                dmc.AccordionPanel(
                                    html.Div(
                                        id="rich_text_output",
                                        style={
                                            "height": "300px",
                                            "overflowY": "scroll",
                                        },
                                    )
                                ),
                            ],
                            value="raw_html",
                        ),
                    ],
                ),
                dmc.Space(h=20),
                dmc.Group(
                    [
                        dmc.Button("Submit", id="modal_submit_new_event_button"),
                        dmc.Button(
                            "Close",
                            color="red",
                            variant="outline",
                            id="modal_close_new_event_button",
                        ),
                    ],
                    position="right",
                ),
            ],
        ),
    ]
)


@app.callback(
    Output("modal", "opened"),
    Output("modal", "title"),
    Output("modal_event_display_context", "children"),
    Input("modal-close-button", "n_clicks"),
    Input("calendar", "clickedEvent"),
    State("modal", "opened"),
)
def open_event_modal(n, clickedEvent, opened):
    ctx = callback_context

    if not ctx.triggered:
        raise PreventUpdate
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "calendar" and clickedEvent is not None:
        event_title = clickedEvent["title"]
        event_context = clickedEvent["extendedProps"]["context"]
        return (
            True,
            event_title,
            html.Div(
                dash_quill.Quill(
                    id="input3",
                    value=f"{event_context}",
                    modules={
                        "toolbar": False,
                        "clipboard": {
                            "matchVisual": False,
                        },
                    },
                ),
                style={"width": "100%", "overflowY": "auto"},
            ),
        )
    elif button_id == "modal-close-button" and n is not None:
        return False, dash.no_update, dash.no_update

    return opened, dash.no_update


@app.callback(
    Output("add_modal", "opened"),
    Output("add_modal_date", "value"),
    Input("calendar", "dateClicked"),
    Input("modal_close_new_event_button", "n_clicks"),
    State("add_modal", "opened"),
)
def open_add_modal(dateClicked, close_clicks, opened):
    ctx = callback_context

    if not ctx.triggered:
        raise PreventUpdate
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "calendar" and dateClicked is not None:
        return True, dateClicked
    elif button_id == "modal_close_new_event_button" and close_clicks is not None:
        return False, dash.no_update

    return opened, dash.no_update


@app.callback(
    Output("calendar", "events"),
    Output("add_modal", "opened", allow_duplicate=True),
    Output("event_name_input", "value"),
    Output("event_color_select", "value"),
    Output("rich_text_input", "value"),
    Input("modal_submit_new_event_button", "n_clicks"),
    State("add_modal_date", "value"),
    State("event_name_input", "value"),
    State("event_color_select", "value"),
    State("rich_text_output", "children"),
    State("calendar", "events"),
)
def add_new_event(n, date, event_name, event_color, event_context, current_events):
    if n is None:
        raise PreventUpdate

    new_event = {
        "title": event_name,
        "start": date,
        "end": date,
        "className": event_color,
        "context": event_context,
    }

    return current_events + [new_event], False, "", "bg-gradient-primary", ""


@app.callback(
    Output("rich_text_output", "children"),
    [Input("rich_text_input", "value")],
    [State("rich_text_input", "charCount")],
)
def display_output(value, charCount):
    return value


if __name__ == "__main__":
    app.run_server(debug=True, port=8056)
