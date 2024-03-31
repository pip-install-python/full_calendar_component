# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fullCalendarComponent <- function(id=NULL, clickedEvent=NULL, dateClicked=NULL, editable=NULL, events=NULL, initialDate=NULL, selectable=NULL) {
    
    props <- list(id=id, clickedEvent=clickedEvent, dateClicked=dateClicked, editable=editable, events=events, initialDate=initialDate, selectable=selectable)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FullCalendarComponent',
        namespace = 'full_calendar_component',
        propNames = c('id', 'clickedEvent', 'dateClicked', 'editable', 'events', 'initialDate', 'selectable'),
        package = 'fullCalendarComponent'
        )

    structure(component, class = c('dash_component', 'list'))
}
