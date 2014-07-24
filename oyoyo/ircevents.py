# Copyright (c) 2011 Duncan Fordyce, Jimmy Cao
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

numeric_events = {
    b"001": "welcome",
    b"002": "yourhost",
    b"003": "created",
    b"004": "myinfo",
    b"005": "featurelist",  # XXX
    b"200": "tracelink",
    b"201": "traceconnecting",
    b"202": "tracehandshake",
    b"203": "traceunknown",
    b"204": "traceoperator",
    b"205": "traceuser",
    b"206": "traceserver",
    b"207": "traceservice",
    b"208": "tracenewtype",
    b"209": "traceclass",
    b"210": "tracereconnect",
    b"211": "statslinkinfo",
    b"212": "statscommands",
    b"213": "statscline",
    b"214": "statsnline",
    b"215": "statsiline",
    b"216": "statskline",
    b"217": "statsqline",
    b"218": "statsyline",
    b"219": "endofstats",
    b"221": "umodeis",
    b"231": "serviceinfo",
    b"232": "endofservices",
    b"233": "service",
    b"234": "servlist",
    b"235": "servlistend",
    b"241": "statslline",
    b"242": "statsuptime",
    b"243": "statsoline",
    b"244": "statshline",
    b"250": "luserconns",
    b"251": "luserclient",
    b"252": "luserop",
    b"253": "luserunknown",
    b"254": "luserchannels",
    b"255": "luserme",
    b"256": "adminme",
    b"257": "adminloc1",
    b"258": "adminloc2",
    b"259": "adminemail",
    b"261": "tracelog",
    b"262": "endoftrace",
    b"263": "tryagain",
    b"265": "n_local",
    b"266": "n_global",
    b"300": "none",
    b"301": "away",
    b"302": "userhost",
    b"303": "ison",
    b"305": "unaway",
    b"306": "nowaway",
    b"311": "whoisuser",
    b"312": "whoisserver",
    b"313": "whoisoperator",
    b"314": "whowasuser",
    b"315": "endofwho",
    b"316": "whoischanop",
    b"317": "whoisidle",
    b"318": "endofwhois",
    b"319": "whoischannels",
    b"321": "liststart",
    b"322": "list",
    b"323": "listend",
    b"324": "channelmodeis",
    b"329": "channelcreate",
    b"331": "notopic",
    b"332": "currenttopic",
    b"333": "topicinfo",
    b"341": "inviting",
    b"342": "summoning",
    b"346": "invitelist",
    b"347": "endofinvitelist",
    b"348": "exceptlist",
    b"349": "endofexceptlist",
    b"351": "version",
    b"352": "whoreply",
    b"353": "namreply",
    b"354": "whospcrpl",
    b"361": "killdone",
    b"362": "closing",
    b"363": "closeend",
    b"364": "links",
    b"365": "endoflinks",
    b"366": "endofnames",
    b"367": "banlist",
    b"368": "endofbanlist",
    b"369": "endofwhowas",
    b"371": "info",
    b"372": "motd",
    b"373": "infostart",
    b"374": "endofinfo",
    b"375": "motdstart",
    b"376": "endofmotd",
    b"377": "motd2",        # 1997-10-16 -- tkil
    b"381": "youreoper",
    b"382": "rehashing",
    b"384": "myportis",
    b"391": "time",
    b"392": "usersstart",
    b"393": "users",
    b"394": "endofusers",
    b"395": "nousers",
    b"396": "event_hosthidden",
    b"401": "nosuchnick",
    b"402": "nosuchserver",
    b"403": "nosuchchannel",
    b"404": "cannotsendtochan",
    b"405": "toomanychannels",
    b"406": "wasnosuchnick",
    b"407": "toomanytargets",
    b"409": "noorigin",
    b"411": "norecipient",
    b"412": "notexttosend",
    b"413": "notoplevel",
    b"414": "wildtoplevel",
    b"421": "unknowncommand",
    b"422": "nomotd",
    b"423": "noadmininfo",
    b"424": "fileerror",
    b"431": "nonicknamegiven",
    b"432": "erroneusnickname", # Thiss iz how its speld in thee RFC.
    b"433": "nicknameinuse",
    b"436": "nickcollision",
    b"437": "unavailresource",  # "Nick temporally unavailable"
    b"441": "usernotinchannel",
    b"442": "notonchannel",
    b"443": "useronchannel",
    b"444": "nologin",
    b"445": "summondisabled",
    b"446": "usersdisabled",
    b"451": "notregistered",
    b"461": "needmoreparams",
    b"462": "alreadyregistered",
    b"463": "nopermforhost",
    b"464": "passwdmismatch",
    b"465": "yourebannedcreep", # I love this one...
    b"466": "youwillbebanned",
    b"467": "keyset",
    b"471": "channelisfull",
    b"472": "unknownmode",
    b"473": "inviteonlychan",
    b"474": "bannedfromchan",
    b"475": "badchannelkey",
    b"476": "badchanmask",
    b"477": "nochanmodes",  # "Channel doesn't support modes"
    b"478": "banlistfull",
    b"481": "noprivileges",
    b"482": "chanoprivsneeded",
    b"483": "cantkillserver",
    b"484": "restricted",   # Connection is restricted
    b"485": "uniqopprivsneeded",
    b"491": "nooperhost",
    b"492": "noservicehost",
    b"501": "umodeunknownflag",
    b"502": "usersdontmatch",
    b"728": "quietlist",
    b"729": "quietlistend"
}

generated_events = [
    # Generated events
    "dcc_connect",
    "dcc_disconnect",
    "dccmsg",
    "disconnect",
    "ctcp",
    "ctcpreply",
]

protocol_events = [
    # IRC protocol events
    "error",
    "join",
    "kick",
    "mode",
    "part",
    "ping",
    "privmsg",
    "privnotice",
    "pubmsg",
    "pubnotice",
    "quit",
    "invite",
    "pong",
]

all_events = generated_events + protocol_events + list(numeric_events.values())
