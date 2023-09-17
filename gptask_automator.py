import openai
import argparse
import configparser

# Settings variables
API_KEY: str
ENGINE: str
TEMPERATURE: float
MAX_FIXING_ATTEMPTS: int
MAX_TOKENS: int

def load_settings():
    config = configparser.ConfigParser()
    config.read('config.ini')
    section = 'SETTINGS'
    global API_KEY
    API_KEY = config.get(section, 'api_key')
    global ENGINE
    ENGINE = config.get(section, 'engine')
    global TEMPERATURE
    TEMPERATURE = float(config.get(section, 'temperature'))
    global MAX_TOKENS
    MAX_TOKENS = int(config.get(section, 'max_tokens'))
    global MAX_FIXING_ATTEMPTS
    MAX_FIXING_ATTEMPTS = int(config.get(section, 'max_fixing_attempts'))

def generate_python_code(prompt: str) -> str:
    openai.api_key = API_KEY

    response = openai.Completion.create(
        engine=ENGINE,
        prompt=prompt,
        max_tokens=MAX_TOKENS,
        stop=None,
        temperature=TEMPERATURE,
    )

    return response.choices[0].text.strip()

def colored_string(string: str, color_code: str) -> str:
    return f'{color_code}{string}\033[0m'

def main():
    parser = argparse.ArgumentParser(description="Generate and execute Python code to solve your tasks using GPT model API.")
    parser.add_argument("--task", help="Specify the action you want to perform", default="")
    args = parser.parse_args()

    # Read configs from the config.ini file
    load_settings()

    # Get action to perform
    if args.task is not None and len(str(args.task)) > 0:
        action = args.task
    else:
        action = input("Specify the action you want to perform: ")

    # Terminate the program if not action is provided
    if len(action) <= 0:
        return

    # Generate Python code using GPT API
    python_code = generate_python_code(f"Generate Python code to {action}")
    print(f"\nGenerated Python code:\n------------------------------")
    print(colored_string(python_code, color_code='\033[32m'))   # Print code with color green
    print('------------------------------\nExecuting...')

    '''
        Execution of code
    '''
    try:
        exec(python_code)
        print('Task Done.')

    except Exception as e:

        '''
            Fixing errors
        '''

        error_str: str = str(e)
        print('Encountered error: ', colored_string(error_str, '\033[91m'))   # Print error with red color
        print('Trying to fix it...')

        # Fixing cycle
        fixed: bool = False
        counter = 0
        while not fixed or counter < MAX_FIXING_ATTEMPTS:
            counter += 1
            python_code = generate_python_code(f"Generate new Python code to {action}. Try to avoid the error i previously got: {error_str}")
            print(f"\nNew Python code:\n------------------------------")
            print(colored_string(python_code, color_code='\033[32m'))   # Print code with color green
            print('------------------------------\nExecuting...')
            try:
                exec(python_code)
                print('Task Done.')
            except Exception as e:
                if counter < MAX_FIXING_ATTEMPTS:
                    error_str: str = str(e)
                    print('Encountered error: ', colored_string(error_str, '\033[91m'))  # Print error with red color
                    print('Trying to fix it...')
                else:
                    print(f'Encountered error: {error_str}.\nMax attempts reached.\nFailed to execute the given task.')


if __name__ == "__main__":
    main()
