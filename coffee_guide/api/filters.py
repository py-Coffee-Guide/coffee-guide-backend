import django_filters

from cafe.models import Cafe, Alternative


class CafeFilter(django_filters.FilterSet):
    """
    /api/v1/cafes/?name=your_filter_name
    /api/v1/cafes/?alternatives=v60&alternatives=chemex&alternatives=aeropress&alternatives=french_press
    /api/v1/cafes/?roasters=Submarine&roasters=The_Welder_Catherine
    /api/v1/cafes/?tags=La_Marzocco
    /api/v1/cafes/?address=your_address
    """

    tags = django_filters.ModelMultipleChoiceFilter(
        field_name="tags__slug",
        to_field_name="name",
    )
    address = django_filters.CharFilter(
        field_name="address__name", lookup_expr="icontains"
    )
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )
    alternatives = django_filters.CharFilter(
        field_name="alternatives__slug", lookup_expr="icontains", queryset=Alternative.objects.all()
    )
    roasters = django_filters.CharFilter(
        field_name="roasters__slug", lookup_expr="icontains"
    )

    class Meta:
        model = Cafe
        fields = ["address", "name", "alternatives", "roasters"]
