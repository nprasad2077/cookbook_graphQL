# Test GraphiQL Queries

```graphQL
query MyQuery {
  categoryByName(name: "Dairy") {
    name
    ingredients {
      name
      notes
    }
  }
}

query MyQueryTwo {
  categoryByName(name: "Meat") {
    name
    ingredients {
      name
      notes
    }
  }
}

query MyQuery3 {
  allIngredients {
    name
    notes
  }
}

query MyQuery4 {
  allIngredients {
    notes
  }
}

query MyQuery5 {
  allIngredients {
    category {
      name
    }
    name
  }
}

query MyQuery6 {
  allIngredients {
    id
    name
  }
}

query MyQuery7 {
  allIngredients {
    name
    category {
      name
    }
  }
}
```
