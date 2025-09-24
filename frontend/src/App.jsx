import { useEffect } from 'react'
import './App.css'
import WebApp from '@twa-dev/sdk'

function App() {
  useEffect(() => {
    WebApp.ready();
    WebApp.expand();
  }, []);

  const handleOrder = (planName, months, price) => {
    const data = {
      plan: planName,
      months: months,
      price: price,
      user_id: WebApp.initDataUnsafe.user?.id || 'unknown',
    };

    console.log('Отправка данных:', data);
    WebApp.sendData(JSON.stringify(data));
  };

  const tariffPlans = [
    { name: '1 месяц', months: 1, price: 100, id: 1 },
    { name: '3 месяца', months: 3, price: 250, id: 2 },
    { name: '6 месяцев', months: 6, price: 450, id: 3 },
    { name: '1 год', months: 12, price: 800, id: 4 },
  ];

  return (
    <div className="app">
      <header className="app-header">
        <h1>Заказ рекламы</h1>
        <p>Выберите срок размещения</p>
      </header>
      <main className="tariff-list">
        {tariffPlans.map((plan) => (
          <div key={plan.id} className="tariff-card">
            <h3>{plan.name}</h3>
            <p className="price">{plan.price} руб.</p>
            <button
              onClick={() => handleOrder(plan.name, plan.months, plan.price)}
              className="order-button"
            >
              Выбрать за {plan.price} руб.
            </button>
          </div>
        ))}
      </main>
      <footer className="app-footer">
        <p>Оплата через ЮКассу (тестовый режим)</p>
      </footer>
    </div>
  )
}

export default App