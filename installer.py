import os
import files

name = 'dns-vault'
projectPath = '../' + name

resources = {
    'readme': {
        'name': 'README.md',
        'source': '/',
        'target': '/',
    },
    'phpunit': {
        'name': 'phpunit.xml',
        'source': '/',
        'target': '/',
    },
    'AppServiceProvider': {
        'name': 'AppServiceProvider.php',
        'source': '/',
        'target': '/app/Providers/',
    },
    'github': {
        'name': '.github',
        'source': '/',
        'target': '/',
    },
    'env-ci': {
        'name': '.env.ci',
        'source': '/',
        'target': '/',
    },
}

environments = {
    'APP_NAME': "Servers",
    'APP_URL': "https://servers.test",
    'SESSION_DOMAIN': "servers.test",
    'SESSION_DRIVER': "database",
    'SESSION_SECURE': "true",
    'DB_PORT': "33072",
    'DB_DATABASE': "laravel",
    'MAIL_HOST': "127.0.0.1",
    'MAIL_PORT': "2525",
    'MAIL_USERNAME': "servers",
    'MAIL_FROM_ADDRESS': "noreply@servers.test",
    'MAIL_FROM_NAME': "Servers",
    'POSTMARK_TOKEN': "token"
}

packages = {
    'DEFAULT': "default",
    'COMPOSER': "composer",
    'NPM': "npm",
    'ARTISAN': "artisan",
    'TESTING': "testing",
}

switchToBasePath = 'cd ../ && '
switchToProjectPath = 'cd ../' + name + '/ && '


def base_command(executionCommand):
    os.system(switchToBasePath + executionCommand)


def project_command(executionCommand):
    os.system(switchToProjectPath + executionCommand)


def remove_project():
    base_command('rm -rf ' + name)


def install_laravel():
    base_command('laravel new ' + name)


def copy_resources():
    for key, value in resources.items():
        source = 'resources' + value['source'] + value['name']
        target = projectPath + value['target'] + value['name']
        files.copy_file(source, target)


def set_variables():
    for key, value in environments.items():
        path = projectPath + '/.env'
        files.update_key_value(path, key, value)


def install_packages():
    file = files.load_json('configuration/packages.json')
    for key, value in packages.items():
        for package in file[value]:
            for command in package['commands']:
                project_command(command['command'])


install_laravel()
copy_resources()
set_variables()
install_packages()
# remove_project()
