import os
import files

name = 'server'

environments = {
    'APP_NAME': "Server",
    'APP_URL': "https://server.test",
    'SESSION_DOMAIN': "server.test",
    'SESSION_DRIVER': "database",
    'DB_PORT': "33072",
    'DB_DATABASE': "laravel",
    'MAIL_PORT': "2525",
    'MAIL_USERNAME': "server",
    'MAIL_FROM_ADDRESS': "noreply@server.test",
    'MAIL_FROM_NAME': "Server",
}

packages = {
    'DEFAULT': "default",
    'COMPOSER': "composer",
    'NPM': "npm",
    'ARTISAN': "artisan",
    'TESTING': "testing",
}

switchToBasePath = 'cd ../ && '
switchToProjectPath = 'cd ../server/ && '


def base_command(executionCommand):
    os.system(switchToBasePath + executionCommand)


def project_command(executionCommand):
    os.system(switchToProjectPath + executionCommand)


def remove_project():
    base_command('rm -rf ' + name)


def install_laravel():
    base_command('laravel new ' + name)


def set_variables():
    for key, value in environments.items():
        files.update_key_value('../server/.env', key, value)


def install_packages():
    file = files.load_json('configuration/packages.json')
    for key, value in packages.items():
        for package in file[value]:
            for command in package['commands']:
                project_command(command['command'])


install_laravel()
files.copy_file('resources/phpunit.xml', '../server/phpunit.xml')
set_variables()
install_packages()
# remove_project()
