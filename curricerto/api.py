from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("/curriculos/", "curriculos.api.router")
