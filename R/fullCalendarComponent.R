# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fullCalendarComponent <- function(id=NULL, businessHours=NULL, clickedEvent=NULL, dateClicked=NULL, editable=NULL, events=NULL, headerToolbar=NULL, initialDate=NULL, initialView=NULL, multiMonthMaxColumns=NULL, navLinks=NULL, nowIndicator=NULL, resources=NULL, selectable=NULL, timeClicked=NULL, views=NULL) {
    
    props <- list(id=id, businessHours=businessHours, clickedEvent=clickedEvent, dateClicked=dateClicked, editable=editable, events=events, headerToolbar=headerToolbar, initialDate=initialDate, initialView=initialView, multiMonthMaxColumns=multiMonthMaxColumns, navLinks=navLinks, nowIndicator=nowIndicator, resources=resources, selectable=selectable, timeClicked=timeClicked, views=views)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FullCalendarComponent',
        namespace = 'full_calendar_component',
        propNames = c('id', 'businessHours', 'clickedEvent', 'dateClicked', 'editable', 'events', 'headerToolbar', 'initialDate', 'initialView', 'multiMonthMaxColumns', 'navLinks', 'nowIndicator', 'resources', 'selectable', 'timeClicked', 'views'),
        package = 'fullCalendarComponent'
        )

    structure(component, class = c('dash_component', 'list'))
}
