# Dictionary Attack Wordlist Generator

## Overview
This project is a Python-based tool designed to generate a custom wordlist for dictionary attacks. It leverages user-provided keywords and customizable parameters to produce password combinations, which can then be saved to a text file. The tool is intended for ethical purposes, such as security testing and penetration testing, to help identify weak or commonly used passwords.

## Features
- Generate password combinations based on:
  - User-provided keywords
  - Customizable minimum and maximum password lengths
  - Inclusion of numbers
  - Inclusion of special characters
- Save generated passwords to a text file for further use.

## Usage
### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dictionary-attack-generator.git
   cd dictionary-attack-generator
   ```
2. Ensure you have Python installed by running:
   ```bash
   python --version
   ```

### Running the Program
1. Execute the script:
   ```bash
   python generate_dictionary.py
   ```
2. Follow the prompts:
   - Enter keywords related to the target, separated by commas (e.g., `name,birthdate,pet`).
   - Specify the minimum and maximum password lengths.
   - Indicate whether to include numbers and/or special characters.
3. The generated wordlist will be saved as `dictionary_attack_wordlist.txt` in the current directory.

### Example
If the following inputs are provided:
- Keywords: `john,12345`
- Minimum length: `6`
- Maximum length: `8`
- Include numbers: `yes`
- Include special characters: `no`

The tool will generate a wordlist containing combinations such as:
- `john12`
- `12345j`
- `j12345`
- ...

## File Structure
```
.
├── generate_dictionary.py  # Main script
├── dictionary_attack_wordlist.txt  # Output file (generated)
└── README.md  # Documentation
```

## Code Explanation
### `generate_dictionary` Function
This function generates password combinations using:
- `itertools.product`: To create all possible combinations of characters for a specified length.
- User-provided parameters: Keywords, length range, and character inclusion options.

### Main Script Workflow
1. Collect user inputs for keywords, length range, and character preferences.
2. Generate combinations using the `generate_dictionary` function.
3. Save the results to `dictionary_attack_wordlist.txt`.

## Limitations
- Large combinations can lead to high memory usage and longer processing times. Ensure your system has adequate resources.
- Use responsibly and only with proper authorization.

## Legal Disclaimer
This tool is intended for educational and ethical purposes only. Unauthorized use of this tool to compromise systems or accounts is illegal and punishable by law. Use only with explicit permission.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

