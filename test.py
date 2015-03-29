from matching import Category, Item, db

cat1 = Category.query.filter_by(name = "Beer").first()

print cat1.name, "NAME"
print cat1.items.all()

print Category.query.all()
beer = Item.query.filter_by(title = "Corona").first()
print beer.title