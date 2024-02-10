import django_filters

from cafe.models import Cafe, Tag


class CafeFilter(django_filters.FilterSet):
    """
    /api/v1/cafe/?name=your_filter_name
    /api/v1/cafe/?alternatives=your_alternative_name
    /api/v1/cafe/?roaster=your_roaster_name
    /api/v1/cafe/?tags=your_tag_name
    /api/v1/cafe/?address=your_address
    """

    tags = django_filters.ModelMultipleChoiceFilter(
        field_name="tag__name", to_field_name="name", queryset=Tag.objects.all()
    )
    address = django_filters.CharFilter(field_name="address", lookup_expr="icontains")
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    alternatives = django_filters.CharFilter(field_name="alternative__name", lookup_expr="icontains")
    roasters = django_filters.CharFilter(field_name="roaster__name", lookup_expr="icontains")

    class Meta:
        model = Cafe
        fields = ["address", "name", "alternatives", "roasters"]
