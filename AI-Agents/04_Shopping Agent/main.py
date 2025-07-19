import requests

class ShoppingAgent:
    def __init__(self):
        # API endpoint for product data
        self.api_url = "https://hackathon-apis.vercel.app/api/products"
        self.products = self.fetch_products()

    def fetch_products(self):
        """
        Fetches product data from the API endpoint.
        Returns a list of products or an empty list if the request fails.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raises an error for bad status codes
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching products: {e}")
            return []

    def search_products(self, query):
        """
        Searches products based on user query.
        Args:
            query (str): User's search query (e.g., "laptop", "price < 500").
        Returns:
            List of matching products or a message if no products are found.
        """
        query = query.lower().strip()
        results = []

        # Handle different types of queries
        for product in self.products:
            name = product.get('name', '').lower()
            price = float(product.get('price', 0))
            description = product.get('description', '').lower()

            # Simple keyword search in name or description
            if query in name or query in description:
                results.append(product)
            # Handle price-based queries (e.g., "price < 500")
            elif query.startswith("price <"):
                try:
                    max_price = float(query.split("<")[1].strip())
                    if price <= max_price:
                        results.append(product)
                except ValueError:
                    continue
            elif query.startswith("price >"):
                try:
                    min_price = float(query.split(">")[1].strip())
                    if price >= min_price:
                        results.append(product)
                except ValueError:
                    continue

        return results if results else "No products found matching your query."

    def process_query(self, user_query):
        """
        Processes the user query and returns a formatted response.
        Args:
            user_query (str): The user's input query.
        Returns:
            Formatted string with product details or a message.
        """
        results = self.search_products(user_query)
        if isinstance(results, str):
            return results

        # Format the response
        response = "Found the following products:\n"
        for product in results:
            response += f"- {product['name']} (Price: ${product['price']})\n"
            response += f"  Description: {product['description']}\n"
        return response

def main():
    # Initialize the agent
    agent = ShoppingAgent()

    # Test queries
    test_queries = [
        "phone"
        "price < 500",
        "laptop"
        "price > 1000",
    ]

    # Process and print results for each test query
    print("Testing Shopping Agent with sample queries:\n")
    for query in test_queries:
        print(f"Query: {query}")
        print(agent.process_query(query))
        print("-" * 50)

if __name__ == "__main__":
    main()