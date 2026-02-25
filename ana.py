import datetime

class RetailAnalytics:
    def __init__(self, current_date):
        self.current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        self.customers = {}

    def ingest_data(self, transactions):
        """
        Processes raw transactions into a structured customer profile.
        Format: {'customer_id': 'ID', 'amount': 100, 'date': 'YYYY-MM-DD'}
        """
        for tx in transactions:
            c_id = tx['customer_id']
            tx_date = datetime.datetime.strptime(tx['date'], "%Y-%m-%d")
            
            if c_id not in self.customers:
                self.customers[c_id] = {'dates': [], 'spent': 0}
            
            self.customers[c_id]['dates'].append(tx_date)
            self.customers[c_id]['spent'] += tx['amount']

    def calculate_metrics(self):
        """Calculates Recency, Frequency, and Monetary (RFM) values."""
        analysis = {}
        for c_id, data in self.customers.items():
            last_purchase = max(data['dates'])
            recency = (self.current_date - last_purchase).days
            frequency = len(data['dates'])
            monetary = data['spent']
            
            # Simple scoring: Higher frequency + Higher spending = Better
            # Higher recency = Bad (At risk)
            score = (frequency * 10) + (monetary / 5) - (recency * 0.5)
            
            analysis[c_id] = {
                "recency": recency,
                "frequency": frequency,
                "monetary": monetary,
                "score": round(score, 2),
                "status": "At Risk" if recency > 30 else "Active"
            }
        return analysis

    def get_report(self):
        """Prints a professional analytical summary."""
        metrics = self.calculate_metrics()
        # Sort by score descending
        sorted_customers = sorted(metrics.items(), key=lambda x: x[1]['score'], reverse=True)

        print(f"{'ID':<10} | {'Spent':<8} | {'Freq':<5} | {'Recency':<8} | {'Status':<8} | {'Score'}")
        print("-" * 65)
        for c_id, m in sorted_customers:
            print(f"{c_id:<10} | ${m['monetary']:<7} | {m['frequency']:<5} | "
                  f"{m['recency']:<3} days | {m['status']:<8} | {m['score']}")

# --- Execution ---
if __name__ == "__main__":
    # Simulated Raw Data
    raw_data = [
        {'customer_id': 'C101', 'amount': 150, 'date': '2026-02-20'},
        {'customer_id': 'C102', 'amount': 50,  'date': '2026-01-05'},
        {'customer_id': 'C101', 'amount': 200, 'date': '2026-02-24'},
        {'customer_id': 'C103', 'amount': 900, 'date': '2026-02-15'},
        {'customer_id': 'C102', 'amount': 30,  'date': '2026-01-10'},
        {'customer_id': 'C104', 'amount': 10,  'date': '2026-02-25'},
    ]

    # Initialize with "Today's Date" (matching the 2026 context)
    engine = RetailAnalytics(current_date="2026-02-25")
    engine.ingest_data(raw_data)
    engine.get_report()