from enum import Enum
class GuiLabel(Enum):

    NO_ALERT = "Nessun errore riscontrato"
    ALERT_TELESCOPE_LOST = "Connessione con il telescopio persa"
    ALERT_TELESCOPE_ERROR = "Errore del telescopio"
    ALERT_CHECK_CURTAINS_SWITCH = "Controllare switch tende - ricalibrazione"
    ALERT_CRAC_ANOMALY = "Anomalia CRaC: stato invalido dei componenti"
    ALERT_TELESCOPE_ROOF = "Attenzione, Telescopio vicino al tetto"
    ALERT_TELESCOPE_ROOF_CLOSING = "Attenzione, Telescopio non in park e tetto in chiusura"
    ALERT_TELESCOPE_OPERATIVE = "Attenzione telescopio operativo: {status}"
    ALERT_CURTAINS_ENABLED = "Attenzione tende aperte"
    ALERT_ROOF_CLOSED = "Attenzione tetto chiuso"
    CURTAIN_DISABLED = "Disattivata"
    CURTAIN_CLOSED = "Chiusa"
    CURTAIN_STOPPED = "Ferma"
    CURTAIN_OPENED = "Aperta"
    CURTAIN_ERROR = "Errore"
    CURTAIN_DANGER = "Pericolo"
    CURTAIN_OPENING = "Apertura"
    CURTAIN_CLOSING = "Chiusura"
    CURTAIN_DISABLING = "Disattivazione"
    TELESCOPE_PARKED = "Parked"
    TELESCOPE_FLATTER = "Flatter"
    TELESCOPE_SECURED = "In Sicurezza"
    TELESCOPE_SYNC_OFF = "No Sync"
    TELESCOPE_SYNC_ON = "Sync On"
    TELESCOPE_NORTHEAST = "NordEst"
    TELESCOPE_EAST = "Est"
    TELESCOPE_SOUTHEAST = "SudEst"
    TELESCOPE_SOUTHWEST = "SudOvest"
    TELESCOPE_WEST = "Ovest"
    TELESCOPE_NORTHWEST = "NordOvest"
    TELESCOPE_ANOMALY = "Anomalia"
    TELESCOPE_ERROR = "Errore"
    TELESCOPE_TRACKING_ON = "Track On"
    TELESCOPE_TRACKING_OFF = "Track Off"
    TELESCOPE_SLEWING_ON = "Slewing On"
    TELESCOPE_SLEWING_OFF = "Slewing Off"
    TELESCOPE_DISCONNECTED = "Disconnesso"
    ROOF_CLOSED = "Chiuso"
    ROOF_OPEN = "Aperto"
    ROOF_OPENING = "Apertura"
    ROOF_CLOSING = "Chiusura"
    ON = "On"
    OFF = "Off"
    STAND_BY = "Standby"


class GuiKey:

    OPEN_ROOF = "R"
    SYNC_TELE = "S"
    PARK_TELE = "P"
    FLAT_TELE = "F"
    CLOSE_ROOF = "T"
    ENABLED_CURTAINS = "1"
    DISABLED_CURTAINS = "0"
    CALIBRATE_CURTAINS = "2"
    SHUTDOWN = "-"
    CONTINUE = "c"
    EXIT = "E"
    TIMEOUT = "__TIMEOUT__"
    PANEL_ON = "L"
    PANEL_OFF = "D"
    LIGHT_ON = "K"
    LIGHT_OFF = "J"
    POWER_ON_TELE = "W"
    POWER_OFF_TELE = "X"
    POWER_ON_CCD = "A"
    POWER_OFF_CCD = "O"