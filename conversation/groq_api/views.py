import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import ConversationSerializer
from groq import Groq
from .models import Conversation


# Conversation API
class ConversationAPIView(APIView):
    """This View gets the message from the user,
    calls groq api and returns the response back to user


    The data is recieved in the following format:
    {"message": "The massage from user"}

    And the response is returned in the following format:
    {"response": "The response from groq api"}
    """

    # only authenticated users can access this api
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        # check if message is empty
        if (
            request.data.get("message") is None
            or request.data.get("message").strip() == ""
        ):
            return Response(
                {"error": "Message cannot be empty."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # validate the incoming message
        conversation_serializer = ConversationSerializer(data=request.data)

        # get the response from api if valid
        if conversation_serializer.is_valid():

            # groq api call
            client = Groq(api_key=os.getenv("GROQ_API_KEY"))
            
            # fetch user previous messages from database
            messages=Conversation.objects.filter(user=request.user).order_by('-created_at')[:5:-1]
            
            # ordered list of messages between user and assistant
            messages_list = []
            
            # create a list of messages from user and assistant to send to groq api
            for message in messages:
                messages_list.append({"role": "user", "content": message.message})
                messages_list.append({"role": "assistant", "content": message.response})
                
            # append the current user message to the list
            messages_list.append({"role": "user", "content": request.data.get("message")})
            
            # make the groq api request
            chat_completion = client.chat.completions.create(
                messages=messages_list,
                model=f"{os.getenv('GROQ_MODEL')}",
            )

            # save the conversation to database
            conversation = conversation_serializer.save(
                user=request.user, response=chat_completion.choices[0].message.content
            )

            # return the response to frontend
            return Response(
                {"response": conversation.response}, status=status.HTTP_201_CREATED
            )

        return Response(status=status.HTTP_400_BAD_REQUEST)
