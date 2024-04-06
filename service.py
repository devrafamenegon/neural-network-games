import requests

class GamesService:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def authenticate(self):

        """
        Obtém o token de acesso da Twitch API.

        Retorna:
            Dicionário com o token de acesso ("access_token") e tempo de expiração ("expires_in").
        """

        # Parâmetros da requisição
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }

        # URL da API
        url = "https://id.twitch.tv/oauth2/token"

        try:
            # Enviando a requisição POST
            response = requests.post(url, data=payload)

            # Verificando o status code
            if response.status_code == 200:
                # Extraindo o token da resposta
                data = response.json()
                return data

            else:
                # Erro na requisição
                raise Exception(f"Erro: {response.status_code} - {response.text}")

        except Exception as e:
            # Erro genérico
            raise Exception(f"Erro ao obter o token: {e}")

    def get_games(self, access_token):
      """Fetches games data from the IGDB API v4.

      Args:
          access_token: Your IGDB API access token.
          client_id: Your IGDB API Client ID.

      Returns:
          A JSON dictionary containing the API response data, or None on error.
      """

      # URL for the games endpoint
      url = "https://api.igdb.com/v4/games"

      # Fields to retrieve (adjust as needed)
      fields = """
      fields age_ratings,aggregated_rating,aggregated_rating_count,alternative_names,artworks,bundles,category,checksum,collection,collections,cover,created_at,dlcs,expanded_games,expansions,external_games,first_release_date,follows,forks,franchise,franchises,game_engines,game_localizations,game_modes,genres,hypes,involved_companies,keywords,language_supports,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites;
      """

      # Headers with access token and client ID
      headers = {
          "Client-ID": self.client_id,
          "Authorization": f"Bearer {access_token}",
          "Accept": "application/json",
      }

      try:
        # Sending the POST request
        response = requests.post(url, data=f"{fields}", headers=headers)

        # Check for successful response
        if response.status_code == 200:
          return response.json()
        else:
          print(f"Error: {response.status_code} - {response.text}")
          return None

      except Exception as e:
        print(f"An error occurred: {e}")
        return None
      
    def get_genres(self, access_token):
        """Fetches genres data from the IGDB API v4.

        Args:
            access_token: Your IGDB API access token.

        Returns:
            A JSON dictionary containing the API response data, or None on error.
        """

        # URL for the genres endpoint
        url = "https://api.igdb.com/v4/genres"

        # Fields to retrieve (adjust as needed)
        fields = """
        fields checksum,created_at,name,slug,updated_at,url;
        """

        # Headers with access token and client ID
        headers = {
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        }

        try:
            # Sending the POST request
            response = requests.post(url, data=f"{fields}", headers=headers)

            # Check for successful response
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
