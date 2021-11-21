from rest_framework.decorators import api_view

@api_view(['GET'])
def get_slice_by_related_image_stack_id(request, related_img_stack_id):
	print ("Kudu kudu")

