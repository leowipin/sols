import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SolsComponent } from './sols.component';

describe('SolsComponent', () => {
  let component: SolsComponent;
  let fixture: ComponentFixture<SolsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SolsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SolsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
