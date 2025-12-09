from ninja import Router
from ninja.security import django_auth

router = Router(auth=django_auth)

router.add_router("/certificacao", "curriculos.routes.certificacao.router")
router.add_router("/experiencia", "curriculos.routes.experiencia.router")
router.add_router("/formacao", "curriculos.routes.formacao.router")
router.add_router("/habilidade", "curriculos.routes.habilidade.router")
router.add_router("/projeto", "curriculos.routes.projeto.router")
