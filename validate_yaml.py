import yaml
import sys

def validate_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            yaml.safe_load(file)
        print(f"✅ {file_path} est valide.")
    except yaml.YAMLError as e:
        print(f"❌ Erreur dans le fichier YAML : {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate_yaml("guasti-grid.yaml")
