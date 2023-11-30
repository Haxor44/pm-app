class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.PaginationHandlerMixin is None:
                self._paginator = None
            else:
                self._paginator = self.PaginationHandlerMixin()
        else:
            pass
        return self._paginator    
    
    def paginate_queryset(self, queryset):     
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,self.request, view=self)    
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)