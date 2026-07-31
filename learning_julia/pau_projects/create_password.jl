# 1. Added missing 'u', 'v', 'w'
digits =    "1234567890"
lowercase = "abcdefghijklmnopqrstuvwxyz"
capitals =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols =   "!'?%&/()=<>*{}[]+-:;"

function create_password(len,
        digs=true,
        lowc=true,
        caps=true,
        symb=true)

    """
    Creates a random password with the available characters
    
    length: int
    digs: bool # digits
    lowc: bool # lowercase
    caps: bool # capitals
    symb: bool # symbols
    """

    alphabet = ""

    # In Julia, you can write 'if condition action end' on one line like this
    if digs == true alphabet = alphabet * digits end
    if lowc == true alphabet = alphabet * lowercase end
    if caps == true alphabet = alphabet * capitals end
    if symb == true alphabet = alphabet * symbols end

    # Handle edge case where someone sets all options to false
    if isempty(alphabet)
        error("You must select at least one character set!")
    end

    password = ""

    for _ in 1:len
        # rand(alphabet) automatically picks one random character safely
        password = password * rand(alphabet)
    end

    return password
end

# Test it out
println(create_password(12))
