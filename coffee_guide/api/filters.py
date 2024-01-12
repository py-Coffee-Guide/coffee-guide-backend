import django_filters

from cafe.models import Cafe, Tag


class CafeFilter(django_filters.FilterSet):
    """
    /api/cafe/?name=your_filter_name
    /api/cafe/?alternative=your_alternative_name
    /api/cafe/?roaster=your_roaster_name
    /api/cafe/?tag=your_tag_name
    /api/cafe/?address=your_address
    """

    tag = django_filters.ModelMultipleChoiceFilter(
        field_name='tag__name', to_field_name='name',
        queryset=Tag.objects.all()
    )
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
    alternative = django_filters.CharFilter(
        field_name='alternative__name', lookup_expr='icontains'
    )
    roaster = django_filters.CharFilter(
        field_name='roaster__name', lookup_expr='icontains'
    )

    class Meta:
        model = Cafe
        fields = ['address', 'name', 'alternative', 'roaster']
