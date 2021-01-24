# encoding: utf-8
def read_all_lines(filename):
    with open(filename, 'r', encoding="utf-8") as fh:
        content = fh.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    return [x.strip() for x in content]

def add_line(file_name, line):
    with open(file_name, 'a', encoding="utf-8") as fh:
        fh.write(quote+'\n')


def load_matches():
    default=read_all_lines('resources/matches-default.txt')
    players=read_all_lines('resources/matches-player.txt')
    roles=read_all_lines('resources/matches-roles.txt')
    # build regex string
    p='|'.join(players) # <@!622701434713931776>
    r='|'.join(roles) # <@&753944326823739413>
    d='|'.join(default)

    return f'([<][@]([!]({p})|[&]({r}))[>])|({d}))'

def get_command(command):
    operation,optype,group =command.split(' ', 3)

    if optype != 'quotes' and optype != 'matches':
        optype = get_op_name(optype)
    if optype == False:
        return f'Unknown command: {command}'

    resource=f'resources/{optype}-{group}.txt'
    return read_all_lines(resource)

def get_op_name(optype):

    if optype == 'match':
        return 'matches'
    elif optype == 'quote':
        return 'quotes'
    else:
        return False

def add_command(command):
    operation,optype,group,value =command.split(' ', 4)

    optype = get_op_name(optype)
    if optype == False:
        return


    resource=f'resources/{optype}-{group}.txt'
    add_line(resource, value)
