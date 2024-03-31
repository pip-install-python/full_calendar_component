# AUTO GENERATED FILE - DO NOT EDIT

export fcc_fullcalendarcomponent

"""
    fcc_fullcalendarcomponent(;kwargs...)

A FullCalendarComponent component.

Keyword arguments:
- `id` (String; optional)
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
- `initialDate` (String; optional)
- `selectable` (Bool; optional)
"""
function fcc_fullcalendarcomponent(; kwargs...)
        available_props = Symbol[:id, :clickedEvent, :dateClicked, :editable, :events, :initialDate, :selectable]
        wild_props = Symbol[]
        return Component("fcc_fullcalendarcomponent", "FullCalendarComponent", "full_calendar_component", available_props, wild_props; kwargs...)
end

