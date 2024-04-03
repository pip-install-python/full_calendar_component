% Auto-generated: do not edit by hand
\name{fullCalendarComponent}

\alias{fullCalendarComponent}

\title{FullCalendarComponent component}

\description{

}

\usage{
fullCalendarComponent(id=NULL, businessHours=NULL, clickedEvent=NULL,
dateClicked=NULL, editable=NULL, events=NULL,
headerToolbar=NULL, initialDate=NULL, initialView=NULL,
multiMonthMaxColumns=NULL, navLinks=NULL, nowIndicator=NULL,
resources=NULL, selectable=NULL, timeClicked=NULL,
views=NULL)
}

\arguments{
\item{id}{Character. }

\item{businessHours}{List of lists containing elements 'daysofweek', 'starttime', 'endtime'.
those elements have the following types:
  - daysofweek (list of numerics; optional)
  - starttime (character; optional)
  - endtime (character; optional)s. }

\item{clickedEvent}{Named list. }

\item{dateClicked}{Character. }

\item{editable}{Logical. }

\item{events}{List of lists containing elements 'title', 'start', 'end', 'classname', 'context'.
those elements have the following types:
  - title (character; optional)
  - start (character; optional)
  - end (character; optional)
  - classname (character; optional)
  - context (character; optional)s. }

\item{headerToolbar}{Named list. }

\item{initialDate}{Character. }

\item{initialView}{Character. }

\item{multiMonthMaxColumns}{Numeric. }

\item{navLinks}{Logical. }

\item{nowIndicator}{Logical. }

\item{resources}{List of lists containing elements 'id', 'title'.
those elements have the following types:
  - id (character; optional)
  - title (character; optional)s. }

\item{selectable}{Logical. }

\item{timeClicked}{Character. }

\item{views}{Named list. }
}

\value{named list of JSON elements corresponding to React.js properties and their values}

