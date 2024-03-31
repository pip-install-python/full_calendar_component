import React from 'react';
import PropTypes from 'prop-types';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';


const FullCalendarComponent = (props) => {
    const {id, initialDate, selectable, editable, events} = props;

    const handleEventClick = (info) => {
        console.log(info.event);
        if (props.setProps) {
            props.setProps({ clickedEvent: info.event });
        }
        // eventClick(info.event);
    };

    const handleDateClick = (info) => {
    if (props.setProps) {
        props.setProps({ dateClicked: info.dateStr });
    }
};

    return (

        <div id={id}>
            <FullCalendar
                plugins={[ dayGridPlugin, interactionPlugin ]}
                initialView="dayGridMonth"
                headerToolbar={{
                    start: 'title',
                    center: '',
                    end: 'today prev,next'
                }}
                selectable={selectable}
                editable={editable}
                initialDate={initialDate}
                events={events}
                views={{
                    month: {
                        titleFormat: { month: 'long', year: 'numeric' }
                    },
                    agendaWeek: {
                        titleFormat: { month: 'long', year: 'numeric', day: 'numeric' }
                    },
                    agendaDay: {
                        titleFormat: { month: 'short', year: 'numeric', day: 'numeric' }
                    }
                }}
                eventClick={handleEventClick}
                dateClick={handleDateClick}
            />
        </div>

    );
}

FullCalendarComponent.defaultProps = {
    events: [],
    initialDate: '2021-12-01',
    selectable: true,
    editable: true,
    clickedEvent: null,
    dateClicked: null,
    setProps: () => {}
};

FullCalendarComponent.propTypes = {
    id: PropTypes.string,
    initialDate: PropTypes.string,
    selectable: PropTypes.bool,
    editable: PropTypes.bool,
    events: PropTypes.arrayOf(PropTypes.shape({
        title: PropTypes.string,
        start: PropTypes.string,
        end: PropTypes.string,
        className: PropTypes.string,
        context: PropTypes.string
    })),
    clickedEvent: PropTypes.object,
    dateClicked: PropTypes.string,
    setProps: PropTypes.func
};

export default FullCalendarComponent;