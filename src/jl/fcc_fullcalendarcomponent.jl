# AUTO GENERATED FILE - DO NOT EDIT

export fcc_fullcalendarcomponent

"""
    fcc_fullcalendarcomponent(;kwargs...)

A FullCalendarComponent component.

Keyword arguments:
- `id` (String; optional)
- `businessHours` (optional): . businessHours has the following type: Array of lists containing elements 'daysOfWeek', 'startTime', 'endTime'.
Those elements have the following types:
  - `daysOfWeek` (Array of Reals; optional)
  - `startTime` (String; optional)
  - `endTime` (String; optional)s
- `clickedEvent` (Dict; optional)
- `dateClicked` (String; optional)
- `editable` (Bool; optional)
- `events` (optional): . events has the following type: Array of lists containing elements 'title', 'start', 'end', 'className', 'context'.
Those elements have the following types:
  - `title` (String; optional)
  - `start` (String; optional)
  - `end` (String; optional)
  - `className` (String; optional)
  - `context` (String; optional)s
- `headerToolbar` (Dict; optional)
- `initialDate` (String; optional)
- `initialView` (String; optional)
- `multiMonthMaxColumns` (Real; optional)
- `navLinks` (Bool; optional)
- `nowIndicator` (Bool; optional)
- `resources` (optional): . resources has the following type: Array of lists containing elements 'id', 'title'.
Those elements have the following types:
  - `id` (String; optional)
  - `title` (String; optional)s
- `selectable` (Bool; optional)
- `views` (Dict; optional)
"""
function fcc_fullcalendarcomponent(; kwargs...)
        available_props = Symbol[:id, :businessHours, :clickedEvent, :dateClicked, :editable, :events, :headerToolbar, :initialDate, :initialView, :multiMonthMaxColumns, :navLinks, :nowIndicator, :resources, :selectable, :views]
        wild_props = Symbol[]
        return Component("fcc_fullcalendarcomponent", "FullCalendarComponent", "full_calendar_component", available_props, wild_props; kwargs...)
end

