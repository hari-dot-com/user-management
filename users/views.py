from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
from .permissions import IsAdmin, IsEditor, IsViewer
from .models import Video
from .serializers import VideoSerializer

# Registration view
@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=201)
    return Response(serializer.errors, status=400)

# Login view (JWT token generation)
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = get_user_model().objects.get(username=username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        else:
            return Response({'message': 'Invalid credentials'}, status=401)
    except get_user_model().DoesNotExist:
        return Response({'message': 'User does not exist'}, status=404)

# User-based viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def change_role(self, request, pk=None):
        user = self.get_object()
        new_role = request.data.get("role")

        if new_role in ['admin', 'editor', 'viewer']:
            user.role = new_role
            user.save()
            return Response({"status": f"Role changed to {new_role}"})
        return Response({"error": "Invalid role"}, status=400)
    
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
