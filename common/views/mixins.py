from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from common.serializers.mixins import DictMixinSerializer


class ExtendedGenericViewSetMixin(GenericViewSet):
    pass


class ListViewSet(ExtendedGenericViewSetMixin, mixins.ListModelMixin):
    pass


class DictListMixin(ListViewSet):
    serializer_class = DictMixinSerializer
    pagination_class = None


class CRUViewSet(ExtendedGenericViewSetMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet, ):
    pass


class CRUDViewSet(CRUViewSet,
                  mixins.DestroyModelMixin, ):
    pass
