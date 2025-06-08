use std::io::{self, Write};
use std::thread;
use std::time::Duration;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;

pub struct ProgressIndicator {
    running: Arc<AtomicBool>,
    test_name: Arc<String>,
}

impl ProgressIndicator {
    pub fn new(test_name: &str) -> Self {
        let running = Arc::new(AtomicBool::new(true));
        let test_name = Arc::new(test_name.to_string());
        let running_clone = running.clone();
        let test_name_clone = test_name.clone();

        thread::spawn(move || {
            let mut elapsed = 0;
            while running_clone.load(Ordering::Relaxed) {
                print!("\r{} running: {:.1}s", test_name_clone, elapsed as f64 / 10.0);
                thread::sleep(Duration::from_millis(100));
                elapsed += 1;
            }
            print!("\r");
        });

        Self { running, test_name }
    }

    pub fn stop(&mut self, _elapsed_time: f64) {
        self.running.store(false, Ordering::Relaxed);
        thread::sleep(Duration::from_millis(150)); // Give time for the last print
    }
} 