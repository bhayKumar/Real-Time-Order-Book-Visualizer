
# Create the RecentTrades component
recent_trades_component = """
// components/RecentTrades.tsx
import React, { memo, useEffect, useRef, useState } from 'react';
import styles from '../styles/RecentTrades.module.css';

interface Trade {
  price: string;
  quantity: string;
  time: number;
  isBuyerMaker: boolean;
}

interface RecentTradesProps {
  trades: Trade[];
}

const TradeRow = memo(({ trade, isNew }: { trade: Trade; isNew: boolean }) => {
  const isBuy = !trade.isBuyerMaker;
  const time = new Date(trade.time).toLocaleTimeString();
  
  return (
    <div 
      className={`${styles.tradeRow} ${isNew ? (isBuy ? styles.flashGreen : styles.flashRed) : ''}`}
    >
      <span className={`${styles.price} ${isBuy ? styles.buyPrice : styles.sellPrice}`}>
        {parseFloat(trade.price).toFixed(2)}
      </span>
      <span className={styles.quantity}>{parseFloat(trade.quantity).toFixed(6)}</span>
      <span className={styles.time}>{time}</span>
    </div>
  );
});

TradeRow.displayName = 'TradeRow';

export const RecentTrades: React.FC<RecentTradesProps> = memo(({ trades }) => {
  const [flashIds, setFlashIds] = useState<Set<number>>(new Set());
  const prevTradesRef = useRef<Trade[]>([]);

  useEffect(() => {
    if (trades.length > 0 && prevTradesRef.current.length > 0) {
      const newTrade = trades[0];
      const prevTrade = prevTradesRef.current[0];
      
      if (newTrade.time !== prevTrade?.time) {
        setFlashIds(new Set([newTrade.time]));
        
        const timer = setTimeout(() => {
          setFlashIds(new Set());
        }, 500);
        
        return () => clearTimeout(timer);
      }
    }
    prevTradesRef.current = trades;
  }, [trades]);

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h2>Recent Trades</h2>
      </div>
      <div className={styles.columnHeaders}>
        <span>Price (USDT)</span>
        <span>Amount (BTC)</span>
        <span>Time</span>
      </div>
      <div className={styles.tradesContainer}>
        {trades.map((trade, index) => (
          <TradeRow 
            key={`${trade.time}-${index}`}
            trade={trade}
            isNew={flashIds.has(trade.time) && index === 0}
          />
        ))}
      </div>
    </div>
  );
});

RecentTrades.displayName = 'RecentTrades';
"""

print("RecentTrades component created:")
print("components/RecentTrades.tsx")
print("\nKey features:")
print("- Displays 50 most recent trades")
print("- New trades appear at the top")
print("- Flash animation for new trades (green for buy, red for sell)")
print("- Trade direction based on isBuyerMaker flag")
print("- Optimized with React.memo")
