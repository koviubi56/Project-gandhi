"""
This is NOT for DDOSing! This is for blocking DDOSs!
Copyright (C) 2021  Koviubi56

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import time
import logging
from colorama import init
init(autoreset=True)


class DDoS:
    def __init__(self, maxInOneSecDOS, maxInOneSecDDOS, warn, critical):
        """
        Set up the DDoS protection

        Args:
            maxInOneSecDOS (int): The number of requests by one user in one second. Recommended: 2-5. This should be smaller than every other parameter.
            maxInOneSecDDOS (int): The number of requests by every user in one second. This should be bigger than the maxInOneSecDOS parameter.
            warn (int): If the number of requests by every user in one second is reaches this number, we say "Maybe DDoS?" This should be bigger than the maxInOneSecD(D)oS parameters.
            critical (int): If the number of requests by every user in one second is reaches this number, we say "DDOS!!" This should be bigger than every other parameter.
        """
        self.max = maxInOneSecDOS
        self.maxddos = maxInOneSecDDOS
        self.warn = warn
        self.critical = critical
        self.time = int(time.time())
        import logging
        logging.basicConfig(
            level=logging.DEBUG, format="[%(levelname)s %(name)s %(asctime)s line: %(lineno)d] %(message)s")
        logging = logging.getLogger(__name__)
        logging.info("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.")
        self.resetDB()

    def resetDB(self, dosdb=True, ddosdb=True):
        """
        Resets the database. It's ran in every second.

        Args:
            dosdb (bool, optional): Reset the self.db variable? Every user, and the number of requests by the user is listed here. Defaults to True.
            ddosdb (bool, optional): Reset the self.ddos variable? There are the number of requests by every user. Defaults to True.
        """
        if dosdb:
            self.db = {}
        if ddosdb:
            self.ddos = 0

    def test(self, identity, justForTest=False):
        """
        Test if the request is spam, is there are (D)DoS.

        Args:
            identity (any): The identity. Please, write a string, but we try to convert it to string if we can. This could be an IP address.
            justForTest (bool, optional): If it's True, we don't store the request in our database. Defaults to False.

        Returns:
            bool: Does the requests spam.
            "ERROR": If we can't convert the identity parameter to string.
        """
        logging.debug(
            f"BEFORE: id=\"{identity}\"; dosdb=\"{self.db}\"; ddosdb=\"{self.ddos}\"")
        if not isinstance(identity, str):
            try:
                goodIndentity = str(identity)
            except:
                logging.error("\033[1;4;37;41mCan't convert {} to string!".format(
                    str(type(identity))))
                return "ERROR"
            else:
                logging.debug("\033[36mConverted {} to string.".format(
                    str(type(identity))))
        else:
            goodIndentity = identity

        if self.time != int(time.time()):
            self.time = int(time.time())
            self.resetDB()

        if justForTest is False:
            try:
                self.db[goodIndentity] += 1
            except KeyError:
                self.db[goodIndentity] = 1

            self.ddos += 1

        logging.debug(
            f"AFTER: id=\"{identity}\"; dosdb=\"{self.db}\"; ddosdb=\"{self.ddos}\"")

        if isinstance(self.warn, int):
            if self.ddos > self.warn:
                logging.warning(
                    "\033[1;31mMaybe DDoS? There are {req} requests!".format(req=self.ddos))
        if isinstance(self.critical, int):
            if self.ddos > self.critical:
                logging.critical("\033[1;37;41m*** DDOS!! ***")
                logging.critical(
                    "\033[1;37;41m* There are {req} requests in this second yet! *".format(req=self.ddos))
                logging.critical("\033[1;37;41m* It CAN be a DDoS! *")
                logging.critical(
                    "\033[1;37;41m* For THIS second, we block EVERY request! *")
                logging.critical("\033[1;37;41m******")

        if self.db[goodIndentity] > self.max:
            logging.info("\033[1;31mIdentity: \"{id}\" have been blocked due to the {req} requests by this person/bot.".format(
                id=goodIndentity, req=str(self.db[goodIndentity])))
            return False
        else:
            if self.ddos > self.maxddos:
                logging.info("\033[1;37;41mIdentity: \"{id}\" have been blocked due to the {req} requests by EVERY user!".format(
                    id=goodIndentity, req=str(self.db[goodIndentity])))
                return False
            logging.debug(
                "\033[32mIdentity: \"{id}\" have been accepted.".format(id=goodIndentity))
            return True


if __name__ == "__main__":
    print("This is not for DDOSinng!")
    print("Try to import this file!")
    print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.")
    while True:
        pass
