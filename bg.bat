: BG (Better Git) is Git, but with less typing.
: Copyright (C) 2021  Koviubi56

: This program is free software: you can redistribute it and/or modify
: it under the terms of the GNU Affero General Public License as published
: by the Free Software Foundation, either version 3 of the License, or
: (at your option) any later version.

: This program is distributed in the hope that it will be useful,
: but WITHOUT ANY WARRANTY; without even the implied warranty of
: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
: GNU Affero General Public License for more details.

: You should have received a copy of the GNU Affero General Public License
: along with this program.  If not, see <https://www.gnu.org/licenses/>.
@echo off
echo/
echo This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
echo/
choice /C YN /T 1 /D Y /M "Exit at end "
set eae=%ERRORLEVEL%
title Choice
choice /C CSLTO /T 5 /D C /M "[C]ommit; Pu[s]h; Pu[l]l; S[t]atus; L[o]g"
if %ERRORLEVEL% == 5 (
    title Log
    git log
    timeout /T 15
)
if %ERRORLEVEL% == 4 (
    title Get status...
    git status
    timeout /T 15
)
if %ERRORLEVEL% == 3 (
    title Pulling...
    git pull
    timeout /T 15
)
if %ERRORLEVEL% == 2 (
    title Pushing...
    git push
    timeout /T 15
)
if %ERRORLEVEL% == 1 (
    title Push after Y/N?
    choice /C YN /T 3 /D Y /M "Push after"
    title Commit message?
    set /p msg="Commit message> "
    title Commiting...
    git commit -am "%msg%"
    if %ERRORLEVEL% == 1 (
        title Pushing...
        git push
    )
    timeout /T 15
)
if %eae% == 1 (
    exit
)