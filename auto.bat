:: This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
:: If a copy of the MPL was not distributed with this file,
:: You can obtain one at http://mozilla.org/MPL/2.0/.
@echo off
echo This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
:1
title 60 sec
timeout /T 60

title Pull...
color 17
git pull

title Push...
color 47
git push

color 07
goto 1