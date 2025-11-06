
# Create CSS modules for styling
home_css = """
/* styles/Home.module.css */
.container {
  min-height: 100vh;
  background: #0b0e11;
  color: #eaecef;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: #1e2329;
  border-bottom: 1px solid #2b3139;
}

.header h1 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.status {
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 4px;
}

.connected {
  color: #0ecb81;
  background: rgba(14, 203, 129, 0.1);
}

.disconnected {
  color: #f6465d;
  background: rgba(246, 70, 93, 0.1);
}

.main {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1rem;
  padding: 1rem 2rem;
  max-width: 1600px;
  margin: 0 auto;
}

.orderBookWrapper,
.tradesWrapper {
  background: #1e2329;
  border-radius: 4px;
  overflow: hidden;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 600px;
  color: #848e9c;
}

@media (max-width: 1024px) {
  .main {
    grid-template-columns: 1fr;
  }
}
"""

orderbook_css = """
/* styles/OrderBook.module.css */
.container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.header {
  padding: 1rem;
  border-bottom: 1px solid #2b3139;
}

.header h2 {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 600;
  color: #eaecef;
}

.orderBookGrid {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 1rem;
  padding: 1rem;
}

.bidsSection,
.asksSection {
  display: flex;
  flex-direction: column;
}

.columnHeaders {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  padding: 0.5rem;
  font-size: 0.75rem;
  color: #848e9c;
  font-weight: 500;
  border-bottom: 1px solid #2b3139;
  margin-bottom: 0.5rem;
}

.orders {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.row {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  padding: 0.375rem 0.5rem;
  font-size: 0.875rem;
  font-family: 'Monaco', 'Courier New', monospace;
}

.depthBar {
  position: absolute;
  top: 0;
  right: 0;
  height: 100%;
  opacity: 0.15;
  transition: width 0.3s ease;
}

.bidBar {
  background: #0ecb81;
}

.askBar {
  background: #f6465d;
}

.price {
  position: relative;
  z-index: 1;
  font-weight: 500;
}

.bidsSection .price {
  color: #0ecb81;
}

.asksSection .price {
  color: #f6465d;
}

.amount,
.total {
  position: relative;
  z-index: 1;
  color: #eaecef;
  text-align: right;
}

.spread {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  border-left: 1px solid #2b3139;
  border-right: 1px solid #2b3139;
}

.spreadValue {
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  font-size: 0.875rem;
  font-weight: 600;
  color: #fcd535;
  letter-spacing: 1px;
}

@media (max-width: 768px) {
  .orderBookGrid {
    grid-template-columns: 1fr;
  }
  
  .spread {
    border: none;
    border-top: 1px solid #2b3139;
    border-bottom: 1px solid #2b3139;
  }
  
  .spreadValue {
    writing-mode: horizontal-tb;
    transform: none;
  }
}
"""

trades_css = """
/* styles/RecentTrades.module.css */
.container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.header {
  padding: 1rem;
  border-bottom: 1px solid #2b3139;
}

.header h2 {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 600;
  color: #eaecef;
}

.columnHeaders {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  padding: 0.5rem 1rem;
  font-size: 0.75rem;
  color: #848e9c;
  font-weight: 500;
  border-bottom: 1px solid #2b3139;
}

.tradesContainer {
  overflow-y: auto;
  max-height: 600px;
  padding: 0.5rem 1rem;
}

.tradesContainer::-webkit-scrollbar {
  width: 6px;
}

.tradesContainer::-webkit-scrollbar-track {
  background: #1e2329;
}

.tradesContainer::-webkit-scrollbar-thumb {
  background: #2b3139;
  border-radius: 3px;
}

.tradesContainer::-webkit-scrollbar-thumb:hover {
  background: #3b4149;
}

.tradeRow {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  padding: 0.375rem 0;
  font-size: 0.875rem;
  font-family: 'Monaco', 'Courier New', monospace;
}

.price {
  font-weight: 500;
}

.buyPrice {
  color: #0ecb81;
}

.sellPrice {
  color: #f6465d;
}

.quantity,
.time {
  color: #eaecef;
  text-align: right;
}

.flashGreen {
  animation: flashGreen 0.5s ease;
}

.flashRed {
  animation: flashRed 0.5s ease;
}

@keyframes flashGreen {
  0% {
    background: rgba(14, 203, 129, 0.3);
  }
  100% {
    background: transparent;
  }
}

@keyframes flashRed {
  0% {
    background: rgba(246, 70, 93, 0.3);
  }
  100% {
    background: transparent;
  }
}
"""

globals_css = """
/* styles/globals.css */
html,
body {
  padding: 0;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,
    Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
}

* {
  box-sizing: border-box;
}

a {
  color: inherit;
  text-decoration: none;
}

html {
  scroll-behavior: smooth;
}
"""

print("CSS Modules created:")
print("- styles/Home.module.css")
print("- styles/OrderBook.module.css")
print("- styles/RecentTrades.module.css")
print("- styles/globals.css")
print("\nStyling features:")
print("- Dark theme (Binance-inspired)")
print("- Minimalistic design")
print("- Responsive layout")
print("- Smooth animations")
print("- Custom scrollbars")
print("- Performance-optimized transitions")
