try:
    db = DAL('sqlite://pesquisa.db')
except:
    db=DAL('gae')
    session.connect(request,response,db=db)


response.generic_patterns = ['*'] if request.is_local else []


from gluon.tools import Mail, Auth, Crud, Service, PluginManager, prettydate
mail = Mail()                                  # mailer
auth = Auth(globals(), db)
auth.define_tables(username=True)                                # authentication/authorization
crud = Crud(globals(),db)                                # for CRUD helpers using auth
service = Service()                            # for json, xml, jsonrpc, xmlrpc, amfrpc
plugins = PluginManager()                      # for configuring plugins

mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
mail.settings.sender = 'you@gmail.com'         # your email
mail.settings.login = 'username:password'      # your credentials or None

auth.settings.hmac_key = 'sha512:4b841008-250d-45e3-82ca-e2edf506c2ab'   # before define_tables()
auth.define_tables()                           # creates all needed tables
auth.settings.mailer = mail                    # for user email verification
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = True
auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['verify_email'])+'/%(key)s to verify your email'
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['reset_password'])+'/%(key)s to reset your password'
auth.define_tables(username=True)


crud.settings.auth = None        # =auth to enforce authorization on crud

if auth.is_logged_in():
    user_id = auth.user.id
    user_name = auth.user.first_name

else:
    user_id = None
    user_name = None


Campos = db.define_table('campos',
    Field('estado', 'string', length=300),
    Field('cidade', 'string', length=100),
    Field('nivel', 'string', length=100),
    Field('salario', 'double', length=100),
    Field('framework', 'string', length=100),
    Field('tipo', 'string', length=100)
)




state_list = ["AC",
"AL",
"AP",
"AM",
"BA",
"CE",
"DF",
"ES",
"GO",
"MA",
"MT",
"MS",
"MG",
"PA",
"PB",
"PR",
"PE",
"PI",
"RJ",
"RN",
"RS",
"RO",
"RR",
"SC",
"SP",
"SE",
"TO"
]


type_list = ["clt", 'pj']
level_list = ["Junior", "Pleno", "Senior", "Outro"]
frame_list = ['Django', 'Pylons', 'Web2Py', 'Plone', 'Outros']
Campos.framework.requires = IS_IN_SET(frame_list)
Campos.estado.requires = IS_IN_SET(state_list)
Campos.nivel.requires = IS_IN_SET(level_list)
Campos.tipo.requires = IS_IN_SET(type_list)
Campos.salario.requires = IS_NOT_EMPTY()


def avg(number1, number2):
    try:
        return float(number1)/float(number2)
    except:
        return 0


