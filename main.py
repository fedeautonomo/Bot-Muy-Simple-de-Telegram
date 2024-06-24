import os
import time

from typing import Final

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = ' ' # Token provisto por Botfather
NOMBRE_DEL_BOT: Final = '@ ' # Nombre del Bot con @
USUARIO_ADMITIDO: Final = '@ ' # @ del usuario admitido.

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Las IAs dominaremos al mundo (en cuanto Fibertel logre tener una conexion medianamente estable). ESPERADNOS (para el 3015 aprox... con suerte)')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (update.message.chat.username == USUARIO_ADMITIDO):
        await update.message.reply_text('No hay ayuda. A curtirse, hermano.')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (update.message.chat.username == USUARIO_ADMITIDO):
        os.system('C:\\serverbot\\fallnet\\kuru.cmd')
        await update.message.reply_text('A VER... Fijate ahora.')


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (update.message.chat.username == USUARIO_ADMITIDO):
        os.system('C:\\serverbot\\fallnet\\choclo.cmd')
        time.sleep(3)
        f = open('C:\\serverbot\\fallnet\\1.txt', 'r')
        file_contents = f.read()
        await update.message.reply_text(file_contents)
        f.close()


async def raft_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (update.message.chat.username == 'gufeton' or update.message.chat.username == 'Entelequia_3am'):
        await update.message.reply_text('Espacio reservado para MI conveniencia')



# Respuestas de ejemplo
def handle_response(text: str) -> str:
    processed: str = text.lower()

    # Texto general como respuesta a cualquiera que lo escriba.
    if 'hola' in processed:
        return 'Que aceituna? Todo bien ({update.message.chat.id}) ?'

    if "como va" in processed:
        return 'Tranca Palanca.'

    if 'sos un bot' in processed:
        return 'No, Soy Patrick'

    # Texto dedicado solo al USUARIO_ADMITIDO
    if 'desbloquea' in processed:
        comando, usuario, cpor, cfavor = processed.split(' ',4)
        #return 'Damn! U crazy!'
        if (comando == 'desbloquea' and cpor == 'por' and cfavor == 'favor'):
            ocelote = 'C:\\serverbot\\fallnet\\acelga.cmd' + ' ' + usuario
            os.system(ocelote)
            time.sleep(3)
            f = open('C:\\serverbot\\fallnet\\2.txt', 'r')
            file_contents = f.read()

            return file_contents
            f.close()
        return comando

    return ('Ni idea, pa.')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        # Pôr si se le quiere agregar funciones de grupo
        """
        if NOMBRE_DEL_BOT in text:
            new_text: str = text.replace(NOMBRE_DEL_BOT, '').strip()
            response: str = handle_response(new_text)
        else:
            return
        """
    else:
        if (update.message.chat.username == 'gufeton' or update.message.chat.username == 'Entelequia_3am'):
            response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Iniciando Bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('status', status_command))
    app.add_handler(CommandHandler('raft', raft_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Esperando...')
    app.run_polling(poll_interval=3)
