import React, { useState } from 'react';
import { Utensils, ShoppingCart, CheckCircle, Clock } from 'lucide-react';

interface MenuItem {
  id: string;
  name: string;
  category: 'Breakfast' | 'Lunch' | 'Snacks' | 'Dinner';
  price: number;
  calories: number;
  dietary: 'Veg' | 'Non-Veg' | 'Vegan';
}

export const CanteenMealPlanner: React.FC = () => {
  const [activeCategory, setActiveCategory] = useState<'Breakfast' | 'Lunch' | 'Snacks' | 'Dinner'>('Lunch');
  const [cart, setCart] = useState<{ item: MenuItem; qty: number }[]>([]);
  const [orderPlaced, setOrderPlaced] = useState(false);

  const menu: MenuItem[] = [
    { id: 'm1', name: 'Paneer Butter Masala Meal Box', category: 'Lunch', price: 120, calories: 550, dietary: 'Veg' },
    { id: 'm2', name: 'Grilled Chicken Deluxe Thali', category: 'Lunch', price: 150, calories: 680, dietary: 'Non-Veg' },
    { id: 'm3', name: 'South Indian Dosa Combo', category: 'Breakfast', price: 70, calories: 380, dietary: 'Vegan' },
    { id: 'm4', name: 'Idli Vada Sambar Plate', category: 'Breakfast', price: 50, calories: 310, dietary: 'Vegan' },
    { id: 'm5', name: 'Vegetable Samosa & Mint Chutney', category: 'Snacks', price: 30, calories: 240, dietary: 'Veg' },
    { id: 'm6', name: 'Cold Coffee & Brownie Combo', category: 'Snacks', price: 90, calories: 410, dietary: 'Veg' },
    { id: 'm7', name: 'Rotis with Dal Tadka & Mix Veg', category: 'Dinner', price: 100, calories: 490, dietary: 'Veg' },
  ];

  const filteredMenu = menu.filter(m => m.category === activeCategory);

  const addToCart = (item: MenuItem) => {
    const existing = cart.find(c => c.item.id === item.id);
    if (existing) {
      setCart(cart.map(c => c.item.id === item.id ? { ...c, qty: c.qty + 1 } : c));
    } else {
      setCart([...cart, { item, qty: 1 }]);
    }
  };

  const totalAmount = cart.reduce((acc, c) => acc + c.item.price * c.qty, 0);

  const handleCheckout = () => {
    if (cart.length === 0) return;
    setOrderPlaced(true);
    setTimeout(() => {
      setCart([]);
      setOrderPlaced(false);
    }, 3000);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-orange-50 text-orange-600 rounded-lg">
            <Utensils className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Cafeteria Meal Planner & Digital Pre-Order</h3>
            <p className="text-xs text-gray-500">View daily hostel mess menus and pre-order canteen express meals</p>
          </div>
        </div>
        <div className="flex bg-gray-100 p-1 rounded-lg">
          {(['Breakfast', 'Lunch', 'Snacks', 'Dinner'] as const).map(cat => (
            <button
              key={cat}
              onClick={() => setActiveCategory(cat)}
              className={`px-3 py-1 text-xs font-medium rounded-md transition-all ${
                activeCategory === cat ? 'bg-white text-orange-600 shadow-sm font-semibold' : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      {orderPlaced ? (
        <div className="p-6 bg-emerald-50 border border-emerald-200 rounded-xl text-center space-y-2">
          <CheckCircle className="w-10 h-10 text-emerald-600 mx-auto" />
          <h4 className="font-bold text-gray-900 text-sm">Order Token #CN-409 Confirmed!</h4>
          <p className="text-xs text-gray-600">Your meal is scheduled for pickup at Counter 2 in 15 minutes. Deducted from Digital Wallet.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
          {/* Menu Items */}
          <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-3">
            {filteredMenu.map(item => (
              <div key={item.id} className="p-3.5 rounded-xl border border-gray-100 bg-gray-50/50 hover:bg-gray-50 transition-colors flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between mb-1">
                    <span className={`text-[10px] font-semibold px-2 py-0.5 rounded-full ${
                      item.dietary === 'Veg' ? 'bg-emerald-50 text-emerald-700' :
                      item.dietary === 'Vegan' ? 'bg-green-50 text-green-700' :
                      'bg-rose-50 text-rose-700'
                    }`}>
                      ● {item.dietary}
                    </span>
                    <span className="text-xs text-gray-400 font-mono">{item.calories} kcal</span>
                  </div>
                  <h4 className="font-semibold text-xs text-gray-900 mb-2">{item.name}</h4>
                </div>

                <div className="flex items-center justify-between pt-2 border-t border-gray-100">
                  <span className="font-bold text-sm text-gray-900 font-mono">₹{item.price}</span>
                  <button
                    onClick={() => addToCart(item)}
                    className="bg-orange-500 hover:bg-orange-600 text-white text-xs font-semibold px-3 py-1.5 rounded-lg transition-colors"
                  >
                    + Add Meal
                  </button>
                </div>
              </div>
            ))}
          </div>

          {/* Express Cart Summary */}
          <div className="bg-gray-50 p-4 rounded-xl border border-gray-100 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between border-b border-gray-200 pb-2 mb-3">
                <span className="font-semibold text-xs text-gray-900 flex items-center gap-1.5">
                  <ShoppingCart className="w-4 h-4 text-orange-600" />
                  Express Meal Tray
                </span>
                <span className="text-xs font-bold text-gray-600">{cart.reduce((a, b) => a + b.qty, 0)} Items</span>
              </div>

              {cart.length === 0 ? (
                <div className="text-center text-gray-400 text-xs py-8">
                  Your express tray is empty. Add delicious meals from the menu!
                </div>
              ) : (
                <div className="space-y-2 max-h-48 overflow-y-auto pr-1">
                  {cart.map(c => (
                    <div key={c.item.id} className="flex justify-between items-center text-xs bg-white p-2 rounded-lg border border-gray-100">
                      <div>
                        <span className="font-medium text-gray-800">{c.item.name}</span>
                        <div className="text-[10px] text-gray-400">Qty: {c.qty}</div>
                      </div>
                      <span className="font-bold text-gray-900 font-mono">₹{c.item.price * c.qty}</span>
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div className="pt-3 border-t border-gray-200 mt-3 space-y-2">
              <div className="flex justify-between text-xs font-bold text-gray-900">
                <span>Total Amount:</span>
                <span className="font-mono text-orange-600">₹{totalAmount}</span>
              </div>
              <button
                onClick={handleCheckout}
                disabled={cart.length === 0}
                className={`w-full py-2 text-xs font-semibold rounded-lg flex items-center justify-center gap-1.5 transition-all ${
                  cart.length > 0 ? 'bg-orange-600 hover:bg-orange-700 text-white shadow-sm' : 'bg-gray-200 text-gray-400 cursor-not-allowed'
                }`}
              >
                <Clock className="w-3.5 h-3.5" />
                Pre-Order Now
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
