import React from 'react';
import PropTypes from 'prop-types';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';
import multiMonthPlugin from '@fullcalendar/multimonth';
import resourceTimelinePlugin from '@fullcalendar/resource-timeline';
import resourceTimeGridPlugin from '@fullcalendar/resource-timegrid';
import interactionPlugin from '@fullcalendar/interaction';

import '../../../style/style.css';



const FullCalendarComponent = (props) => {
    const {id, initialView, headerToolbar, initialDate, selectable, editable, events, views, multiMonthMaxColumns, resources, navLinks, businessHours, nowIndicator} = props;

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

    const handleTimeClick = (info) => {
    if (props.setProps) {
        props.setProps({ timeClicked: info.timeStr });
    }
};

    return (

        <div id={id}>
            <FullCalendar
                plugins={[ dayGridPlugin, timeGridPlugin, listPlugin, multiMonthPlugin, interactionPlugin, resourceTimelinePlugin, resourceTimeGridPlugin ]}
                initialView={initialView}
                headerToolbar={headerToolbar}
                selectable={selectable}
                editable={editable}
                initialDate={initialDate}
                events={events}
                multiMonthMaxColumns={multiMonthMaxColumns}
                // themeSystem='darkly'
                resources={resources}
                views={views}
                navLinks={navLinks}
                businessHours={businessHours}
                nowIndicator={nowIndicator}
                // views={{
                //     month: {
                //         titleFormat: { month: 'long', year: 'numeric' }
                //     },
                //     agendaWeek: {
                //         titleFormat: { month: 'long', year: 'numeric', day: 'numeric' }
                //     },
                //     agendaDay: {
                //         titleFormat: { month: 'short', year: 'numeric', day: 'numeric' }
                //     }
                // }}
                eventClick={handleEventClick}
                dateClick={handleDateClick}
                slotClick={handleTimeClick}
            />
        </div>

    );
}

FullCalendarComponent.defaultProps = {
    initialView: 'dayGridMonth',
    headerToolbar: {
        start: 'title',
        center: '',
        end: 'today prev,next'
    },
    events: [],
    initialDate: '2021-12-01',
    selectable: true,
    editable: true,
    businessHours: [],
    nowIndicator: true,
    navLinks: true,
    multiMonthMaxColumns: 2,
    clickedEvent: null,
    dateClicked: null,
    timeClicked: null,
    views: {},
    resources: [],
    setProps: () => {}
};

FullCalendarComponent.propTypes = {
    id: PropTypes.string,
    initialView: PropTypes.string,
    headerToolbar: PropTypes.object,
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
    views: PropTypes.object,
    resources: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.string,
        title: PropTypes.string
    })),
    businessHours: PropTypes.arrayOf(PropTypes.shape({
        daysOfWeek: PropTypes.arrayOf(PropTypes.number),
        startTime: PropTypes.string,
        endTime: PropTypes.string
    })),
    nowIndicator: PropTypes.bool,
    navLinks: PropTypes.bool,
    multiMonthMaxColumns: PropTypes.number,
    clickedEvent: PropTypes.object,
    dateClicked: PropTypes.string,
    timeClicked: PropTypes.string,
    setProps: PropTypes.func,
};

export default FullCalendarComponent;