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
                lines.append(line.replace('\n', '').replace('\r', ''))
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
            file_credits.write(line + '\n')


def get_credits():
    filename_credits = sysinterface.homedir + '/.initproject'
    dev_credits = loadlines(filename_credits, (1,2))
    if dev_credits == None or sysinterface.cmdflag in ('-n','--new-author'):
        dev_credits = ['','']
    while dev_credits[0] == '':
        dev_credits[0] = input('Please, enter your name: ')
    while dev_credits[1] == '':
        dev_credits[1] = input('Please, enter your email: ')
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
    lines.append('# Starting script, imports and calls the main function from the app module.')
    lines.append('import ' + pkg_name + '.main')
    lines.append('')
    lines.append('if __name__ == "__main__":')
    lines.append('\t' + pkg_name + '.main.main()')
    lines.append('')
    savelines(root_path + '/' + launch_name + '.py', lines)

    # pkg init
    lines = ['name = "' + pkg_name + '"']
    lines.append('')
    savelines(pkg_path + '/' + '__init__' + '.py', lines)

    # pkg Main.py
    lines = ['# Main script module.']
    lines.append('')
    savelines(pkg_path + '/' + 'main' + '.py', lines)

    # AUTHORS
    lines = [devname, devemail]
    lines.append('')
    savelines(root_path + '/' + 'AUTHORS', lines)

    # README.md
    lines = ['# README.md of your project. Consists of description, installation and usage tips, troubleshooting, etc.']
    lines.append('')
    savelines(root_path + '/' + 'README.md', lines)

    # LICENSE
    lines = ['# Copy the text of your license of choice here.']
    lines.append('')
    savelines(root_path + '/' + 'LICENSE', lines)

    # setup.py
    lines = []
    lines.append('import setuptools')
    lines.append('import os')
    lines.append('')
    lines.append('with open("README.md", "r") as fh:')
    lines.append('\tlong_description = fh.read()')
    lines.append('')
    lines.append('setuptools.setup(')
    lines.append('\tname="' + launch_name + '",')
    lines.append('\tversion="0.0.1",')
    lines.append('\tauthor="' + devname + '",')
    lines.append('\tauthor_email="' + devemail + '",')
    lines.append('\tdescription="Project description here",')
    lines.append('\tlong_description=long_description,')
    lines.append('\tlong_description_content_type="text/markdown",')
    lines.append('\turl="https://github.com/' + devname + '/' + launch_name + '",')
    lines.append('\tpackages=setuptools.find_packages(),')
    lines.append(')')
    lines.append('')
    savelines(root_path + '/' + 'setup.py', lines)


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
