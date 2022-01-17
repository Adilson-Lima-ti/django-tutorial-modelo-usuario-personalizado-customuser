python3 -m venv venv;
echo "Ambiente virtual instalado"
source venv/bin/activate;
echo "Ambiente virtual ativado"
pip install -r requirements.txt;
pre-commit install;