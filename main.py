from service import GamesService

clientId = "yntu7m99py8fgk79ifjqa47y6xivku"
clientSecret = "on60knm54nlv3kmptfogfxkgh9fpu0"

gamesService = GamesService(client_id=clientId, client_secret=clientSecret)
token = gamesService.authenticate()
games = gamesService.get_games(access_token=token["access_token"])
genres = gamesService.get_genres(access_token=token["access_token"])

print(genres)