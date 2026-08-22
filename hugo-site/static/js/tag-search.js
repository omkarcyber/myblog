document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.sidebar-menu').forEach(function (menu) {
    var search = document.querySelector('.sidebar-tag-search');
    if (!search) {
      return;
    }

    var items = Array.from(menu.querySelectorAll('a[href*="/tags/"]')).filter(function (link) {
      return !/\/tags\/?$/.test(link.getAttribute('href'));
    }).map(function (link) {
      return link.closest('li');
    });

    search.addEventListener('input', function () {
      var query = search.value.trim().toLowerCase();
      var visible = 0;

      items.forEach(function (item) {
        var label = item.querySelector('td').textContent.toLowerCase();
        var matches = !query || label.indexOf(query) !== -1;
        item.hidden = !matches;
        visible += matches ? 1 : 0;
      });

      var empty = menu.querySelector('.sidebar-tag-search-empty');
      if (empty) {
        empty.hidden = visible !== 0;
      }
    });
  });
});
