class Color:
    # --- Reset ---
    RESET = "\033[0m"

    # --- Text Colors ---
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

    # --- Bright Text Colors ---
    BRIGHT_BLACK   = "\033[90m"  # (gray)
    BRIGHT_RED     = "\033[91m"
    BRIGHT_GREEN   = "\033[92m"
    BRIGHT_YELLOW  = "\033[93m"
    BRIGHT_BLUE    = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN    = "\033[96m"
    BRIGHT_WHITE   = "\033[97m"

    # --- Background Colors ---
    BG_BLACK   = "\033[40m"
    BG_RED     = "\033[41m"
    BG_GREEN   = "\033[42m"
    BG_YELLOW  = "\033[43m"
    BG_BLUE    = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN    = "\033[46m"
    BG_WHITE   = "\033[47m"

    # --- Bright Background Colors ---
    BG_BRIGHT_BLACK   = "\033[100m"
    BG_BRIGHT_RED     = "\033[101m"
    BG_BRIGHT_GREEN   = "\033[102m"
    BG_BRIGHT_YELLOW  = "\033[103m"
    BG_BRIGHT_BLUE    = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN    = "\033[106m"
    BG_BRIGHT_WHITE   = "\033[107m"

    # --- Styles ---
    BOLD      = "\033[1m"
    DIM       = "\033[2m"
    ITALIC    = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK     = "\033[5m"
    INVERSE   = "\033[7m"  # swaps fg and bg
    STRIKE    = "\033[9m"


s = Color.BRIGHT_GREEN + " [✓] "
e = Color.BRIGHT_RED + " [✗] "
w = Color.BRIGHT_YELLOW + " [!] "
i = Color.BRIGHT_CYAN + " [i] "

# --- SUCCESS ---
SUCCESS_DATA_FOUND   = s + Color.WHITE + "Data found"   + Color.RESET
SUCCESS_DATA_CREATED = s + Color.WHITE + "Data created" + Color.RESET
SUCCESS_DATA_UPDATED = s + Color.WHITE + "Data updated" + Color.RESET
SUCCESS_DATA_DELETED = s + Color.WHITE + "Data deleted" + Color.RESET

# --- ERRORS ---
ERROR_DATA_NOT_FOUND      = e + Color.WHITE + "Data not found"       + Color.RESET
ERROR_DATA_ALREADY_EXISTS = e + Color.WHITE + "Data already exists"  + Color.RESET
ERROR_DATA_NOT_CREATED    = e + Color.WHITE + "Data not created"     + Color.RESET
ERROR_DATA_NOT_UPDATED    = e + Color.WHITE + "Data not updated"     + Color.RESET
ERROR_DATA_NOT_DELETED    = e + Color.WHITE + "Data not deleted"     + Color.RESET
ERROR_INVALID_INPUT       = e + Color.WHITE + "Invalid input"        + Color.RESET
ERROR_PERMISSION_DENIED   = e + Color.WHITE + "Permission denied"    + Color.RESET
ERROR_CONNECTION_FAILED   = e + Color.WHITE + "Connection failed"    + Color.RESET
ERROR_QUERY_FAILED        = e + Color.WHITE + "Query failed"         + Color.RESET
ERROR_UNKNOWN             = e + Color.WHITE + "Unknown error"        + Color.RESET

# --- WARNINGS ---
WARNING_DATA_EMPTY        = w + Color.WHITE + "Data is empty"        + Color.RESET
WARNING_DATA_TRUNCATED    = w + Color.WHITE + "Data truncated"       + Color.RESET
WARNING_DEPRECATED        = w + Color.WHITE + "Deprecated usage"     + Color.RESET
WARNING_CONNECTION_SLOW   = w + Color.WHITE + "Connection is slow"   + Color.RESET
WARNING_DUPLICATE_ENTRY   = w + Color.WHITE + "Duplicate entry"      + Color.RESET

# --- INFO ---
INFO_CONNECTING           = i + Color.WHITE + "Connecting..."        + Color.RESET
INFO_DISCONNECTING        = i + Color.WHITE + "Disconnecting..."     + Color.RESET
INFO_FETCHING             = i + Color.WHITE + "Fetching data..."     + Color.RESET
INFO_PROCESSING           = i + Color.WHITE + "Processing..."        + Color.RESET
INFO_DONE                 = i + Color.WHITE + "Done"                 + Color.RESET