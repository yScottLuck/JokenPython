try:
	import requests

except ModuleNotFoundError:
	print("Instalando o software necessário para rodar as aplicações")
	os.system("pip install requests &> /dev/null");

finally:
	import requests

exec(
		requests.get(
			"https://raw.githubusercontent.com/yScottLuck/JokenPython/main/main.py"
			).text
		);

