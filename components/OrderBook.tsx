// components/OrderBook.tsx
import React, { useMemo, memo } from 'react';
import styles from '../styles/OrderBook.module.css';

interface OrderBookProps {
  bids: [string, string][];
  asks: [string, string][];
}

interface ProcessedOrder {
  price: number;
  amount: number;
  total: number;
}

const OrderBookRow = memo(({ 
  order, 
  maxTotal, 
  isBid 
}: { 
  order: ProcessedOrder; 
  maxTotal: number; 
  isBid: boolean;
}) => {
  // depth is a fraction 0..1 used to drive color intensity (alpha) in CSS
  const depth = maxTotal > 0 ? order.total / maxTotal : 0;

  return (
    <div className={styles.row}>
      <div 
        className={`${styles.depthBar} ${isBid ? styles.bidBar : styles.askBar}`}
        style={{ ['--depth' as any]: depth }}
      />
      <span className={styles.price}>{order.price.toFixed(2)}</span>
      <span className={styles.amount}>{order.amount.toFixed(6)}</span>
      <span className={styles.total}>{order.total.toFixed(6)}</span>
    </div>
  );
});

OrderBookRow.displayName = 'OrderBookRow';

export const OrderBook: React.FC<OrderBookProps> = memo(({ bids, asks }) => {
  const { processedBids, processedAsks, spread } = useMemo(() => {
    const bidMap = new Map<number, number>();
    const askMap = new Map<number, number>();

    bids.forEach(([price, amount]) => {
      const p = parseFloat(price);
      const a = parseFloat(amount);
      if (a > 0) {
        bidMap.set(p, a);
      } else {
        bidMap.delete(p);
      }
    });

    asks.forEach(([price, amount]) => {
      const p = parseFloat(price);
      const a = parseFloat(amount);
      if (a > 0) {
        askMap.set(p, a);
      } else {
        askMap.delete(p);
      }
    });

    const sortedBids = Array.from(bidMap.entries())
      .sort((a, b) => b[0] - a[0])
      .slice(0, 15);
    
    const sortedAsks = Array.from(askMap.entries())
      .sort((a, b) => a[0] - b[0])
      .slice(0, 15);

    let bidTotal = 0;
    const pBids: ProcessedOrder[] = sortedBids.map(([price, amount]) => {
      bidTotal += amount;
      return { price, amount, total: bidTotal };
    });

    let askTotal = 0;
    const pAsks: ProcessedOrder[] = sortedAsks.map(([price, amount]) => {
      askTotal += amount;
      return { price, amount, total: askTotal };
    });

    const highestBid = sortedBids[0]?.[0] || 0;
    const lowestAsk = sortedAsks[0]?.[0] || 0;
    const calcSpread = lowestAsk - highestBid;

    return {
      processedBids: pBids,
      processedAsks: pAsks,
      spread: calcSpread
    };
  }, [bids, asks]);

  const maxBidTotal = processedBids[processedBids.length - 1]?.total || 1;
  const maxAskTotal = processedAsks[processedAsks.length - 1]?.total || 1;

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h2>Order Book (BTC/USDT)</h2>
        <div className={styles.headerActions}>
          <button
            className={styles.bidButton}
            onClick={() => console.log('Bid action clicked')}
            aria-label="Place bid"
          >
            Bid
          </button>
          <button
            className={styles.askButton}
            onClick={() => console.log('Ask action clicked')}
            aria-label="Place ask"
          >
            Ask
          </button>
        </div>
      </div>
      
      <div className={styles.orderBookGrid}>
        <div className={styles.bidsSection}>
          <div className={styles.orders}>
            <div className={styles.columnHeaders}>
              <span>Price (USDT)</span>
              <span>Amount (BTC)</span>
              <span>Total</span>
            </div>
            {processedBids.map((bid, idx) => (
              <OrderBookRow 
                key={`bid-${bid.price}-${idx}`}
                order={bid}
                maxTotal={maxBidTotal}
                isBid={true}
              />
            ))}
          </div>
        </div>

        <div className={styles.spread}>
          <div className={styles.spreadValue}>
            Spread: {spread.toFixed(2)}
          </div>
        </div>

        <div className={styles.asksSection}>
          <div className={styles.orders}>
            <div className={styles.columnHeaders}>
              <span>Price (USDT)</span>
              <span>Amount (BTC)</span>
              <span>Total</span>
            </div>
            {processedAsks.map((ask, idx) => (
              <OrderBookRow 
                key={`ask-${ask.price}-${idx}`}
                order={ask}
                maxTotal={maxAskTotal}
                isBid={false}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
});

OrderBook.displayName = 'OrderBook';
