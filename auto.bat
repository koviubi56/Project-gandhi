:: This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
:: If a copy of the MPL was not distributed with this file,
:: You can obtain one at http://mozilla.org/MPL/2.0/.
@echo off
echo This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
:1
timeout /T 60

title Pull...
git pull
timeout /T 3

title Push...
git push
timeout /T 3

goto 1