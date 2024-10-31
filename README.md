# rdesktop Connection Wizard

This Python-based CLI tool simplifies the process of connecting to remote desktops using rdesktop. It provides an interactive wizard to generate and execute rdesktop commands with customizable options.

## Features

- Interactive prompt for rdesktop connection settings
- Option to use default settings for quick setup
- Custom configuration for keyboard layout and fullscreen mode
- Automatic retrieval of remote host from environment variable
- Direct execution of the generated rdesktop command
- Checks for rdesktop installation before running
- Provides information about toggling fullscreen mode

## Usage

Run the script from the command line:

```
./rdesktop-conn-wizard.py
```

Follow the prompts to configure your rdesktop connection.

### Default Settings

- Keyboard layout: en-us
- Fullscreen mode: Enabled
- Local X cursor: Enabled

You can change these defaults by modifying the `DEFAULT_KEYBOARD` and `DEFAULT_FULLSCREEN` variables in the script.

### Environment Variable

Set the `RDESKTOP_REMOTE_HOST` environment variable to automatically use a specific remote host:

```
export RDESKTOP_REMOTE_HOST=your_remote_host_ip_or_name
```

### Fullscreen Mode

By default, the connection will be established in fullscreen mode. The wizard informs you that fullscreen mode can be toggled at any time during the session using `Ctrl-Alt-Enter`.

## Example

```
$ RDESKTOP_REMOTE_HOST="192.0.2.10" ./rdesktop-conn-wizard.py
rdesktop Connection Wizard
==========================
Use default settings? (Y/n) [Y]:
Username (include domain if necessary, e.g., DOMAIN\\user): DOMAIN\\zinrai
Using Remote host from environment: 192.0.2.10
Do you want to execute this command now? (Y/n) [Y]:

Generated rdesktop command:
rdesktop -f -k en-us -u DOMAIN\\zinrai 192.0.2.10

Note: Fullscreen mode can be toggled at any time using Ctrl-Alt-Enter.

Executing rdesktop...
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.
