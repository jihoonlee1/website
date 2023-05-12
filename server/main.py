import bottle
import routes


@bottle.get("/static/<filepath:path>")
def static_file(filepath):
	return bottle.static_file(filepath, root="../static")


def main():
	bottle.run(port=8000, reloader=True, debug=True)


if __name__ == "__main__":
	main()
