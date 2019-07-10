from brew_view.authorization import authenticated, Permissions
from brew_view.base_handler import BaseHandler
from brew_view.thrift import ThriftClient


class CommandAPI(BaseHandler):
    @authenticated(permissions=[Permissions.COMMAND_READ])
    async def get(self, command_id):
        """
        ---
        summary: Retrieve a specific Command
        parameters:
          - name: command_id
            in: path
            required: true
            description: The ID of the Command
            type: string
        responses:
          200:
            description: Command with the given ID
            schema:
              $ref: '#/definitions/Command'
          404:
            $ref: '#/definitions/404Error'
          50x:
            $ref: '#/definitions/50xError'
        tags:
          - Commands
        """
        async with ThriftClient() as client:
            thrift_response = await client.getCommand(command_id)

        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(thrift_response)


class CommandListAPI(BaseHandler):
    @authenticated(permissions=[Permissions.COMMAND_READ])
    async def get(self):
        """
        ---
        summary: Retrieve all Commands
        responses:
          200:
            description: All Commands
            schema:
              type: array
              items:
                $ref: '#/definitions/Command'
          50x:
            $ref: '#/definitions/50xError'
        tags:
          - Commands
        """
        async with ThriftClient() as client:
            thrift_response = await client.getCommands()

        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(thrift_response)
