# Main script module.
import initproject_pkg.sysinterface

sysinterface = initproject_pkg.sysinterface.SysInterface()


def print_title():
    print('\n\n')
    print('INITPROJECT, v0.0.1\n')
    print('by Sprottenfraulein (mslaimagulbe@gmail.com).')
    print('\n')


def print_help():
    print('\n\ninitproject [project_name] [-n/-h]\n\nPython project structure initialization tool.\n\n\
    -h\t--help\t\t\tThis help message.\n\
    -n\t--new-author\t\tInput new credits info.\n\n')


def quit_app():
    print("Sorry, Initproject has no permission to create files and folders in this directory!\nPlease try \
    again somewhere else or change the permission rules!")
    exit()


def loadlines(filename, numbers):
    lines = []
    try:
        file_credits = open(filename, 'r')
    except FileNotFoundError:
        return None
    with file_credits:
        for i, line in enumerate(file_credits):
            if i + 1 in numbers:
                lines.append(line)
    while len(lines) < len(numbers):
        lines.append('')
    return lines


def savelines(filename, lines):
    try:
        file_credits = open(filename, 'w')
    except PermissionError:
        quit_app()
    with file_credits:
        for line in lines:
            file_credits.write(line)


def get_credits():
    filename_credits = sysinterface.homedir + '/.initproject'
    dev_credits = loadlines(filename_credits, (1,2))
    if dev_credits == None or sysinterface.cmdflag in ('-n','--new-author'):
        dev_credits = ['','']
    while dev_credits[0] == '':
        dev_credits[0] = input('Please, enter your name: ') + '\n'
    while dev_credits[1] == '':
        dev_credits[1] = input('Please, enter your email: ') + '\n'
    savelines(filename_credits, dev_credits)
    return dev_credits


def makestructure(ROOT_DIR, current_dir, proj_name, devname, devemail):
    root_name = proj_name.title()
    pkg_name = proj_name.lower() + '_pkg'
    launch_name = proj_name.lower()

    sysinterface.createpath((root_name, pkg_name, 'test'))

    root_path = current_dir + '/' + root_name
    pkg_path = root_path + '/' + pkg_name

    # Launcher
    lines = []
    lines.append('# Starting script, imports and calls the main function from the app module.' + '\n')
    lines.append('import ' + pkg_name + '.main' + '\n')
    lines.append('' + '\n')
    lines.append('if __name__ == "__main__":' + '\n')
    lines.append('\t' + pkg_name + '.main.main()' + '\n')
    lines.append('' + '\n')
    savelines(root_path + '/' + launch_name + '.py', lines)

    # pkg init
    lines = ['name = "' + pkg_name + '"' + '\n']
    lines.append('' + '\n')
    savelines(pkg_path + '/' + '__init__' + '.py', lines)

    # pkg Main.py
    lines = ['# Main script module.' + '\n']
    lines.append('' + '\n')
    savelines(pkg_path + '/' + 'main' + '.py', lines)

    # AUTHORS
    lines = [devname + '\n', devemail + '\n']
    lines.append('' + '\n')
    savelines(root_path + '/' + 'AUTHORS', lines)

    # README.md
    lines = ['# README.md of your project. Consists of description, installation and usage tips, troubleshooting, etc.' + '\n']
    lines.append('' + '\n')
    savelines(root_path + '/' + 'README.md', lines)

    # LICENSE
    lines = ['# Copy the text of your license of choice here.' + '\n']
    lines.append('' + '\n')
    savelines(root_path + '/' + 'LICENSE', lines)


def print_success(proj_name):
    print('\nInitialized "' + proj_name.title() + '" successfully.\nThanks for using Initproject!\n\n')


# Script title
def main():
    if sysinterface.cmdflag in ('/?', '-h', '--help') or sysinterface.cmdargument in ('/?', '-h', '--help'):
        print_help()
        exit()
    else:
        print_title()

    current_dir = sysinterface.dirpath
    proj_name = sysinterface.cmdargument

    if not proj_name or proj_name == '':
        print('\nPlease specify a name for your project. For example:\n\npython3 initproject.py my_project\n')
        exit()

    devname, devemail = get_credits()

    makestructure(sysinterface.ROOT_DIR, current_dir, proj_name, devname, devemail)

    print_success(proj_name)
